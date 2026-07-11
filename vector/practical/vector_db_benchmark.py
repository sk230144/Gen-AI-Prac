"""
Phase 0.4 Practical — Brute-force numpy vs Chroma (HNSW-based vector DB)

Goal: FEEL why vector databases exist. We generate random vectors, search
for the nearest ones using pure numpy (brute-force), then do the same
search using Chroma (a real vector DB), and compare speed as the number
of vectors grows.
"""

import time
import numpy as np
import chromadb

DIM = 384          # typical small embedding size
N_VECTORS_LIST = [1_000, 10_000, 100_000]  # grows each round
TOP_K = 5


def make_random_vectors(n, dim):
    # random unit vectors, so cosine similarity ~= dot product (see notes point 7)
    vecs = np.random.randn(n, dim).astype("float32")
    vecs /= np.linalg.norm(vecs, axis=1, keepdims=True)
    return vecs


def brute_force_search(query, vectors, k=TOP_K):
    """Pure numpy cosine similarity search — no index, checks EVERY vector."""
    # vectors are already normalized, so dot product == cosine similarity
    scores = vectors @ query          # (N, DIM) @ (DIM,) -> (N,) dot products
    top_k_idx = np.argsort(-scores)[:k]   # sort descending, take top k
    return top_k_idx, scores[top_k_idx]


def chroma_search(collection, query, k=TOP_K):
    """Chroma uses HNSW under the hood — an approximate index, not brute force."""
    result = collection.query(query_embeddings=[query.tolist()], n_results=k)
    return result["ids"][0], result["distances"][0]


def run_benchmark():
    client = chromadb.Client()  # in-memory, ephemeral — fine for this experiment

    for n in N_VECTORS_LIST:
        print(f"\n=== {n:,} vectors ===")
        vectors = make_random_vectors(n, DIM)
        query = make_random_vectors(1, DIM)[0]

        # ---- Brute-force numpy ----
        start = time.perf_counter()
        bf_idx, bf_scores = brute_force_search(query, vectors)
        bf_time = time.perf_counter() - start
        print(f"Brute-force numpy: {bf_time*1000:.3f} ms  | top match idx={bf_idx[0]} score={bf_scores[0]:.4f}")

        # ---- Chroma (HNSW) ----
        collection = client.get_or_create_collection(name=f"bench_{n}")
        ids = [str(i) for i in range(n)]

        # Chroma insert also takes time — measure separately from query time
        start = time.perf_counter()
        # batch insert to avoid overwhelming it in one call
        batch_size = 5000
        for i in range(0, n, batch_size):
            collection.add(
                ids=ids[i:i+batch_size],
                embeddings=vectors[i:i+batch_size].tolist(),
            )
        insert_time = time.perf_counter() - start
        print(f"Chroma insert time: {insert_time:.3f} s")

        start = time.perf_counter()
        chroma_ids, chroma_dists = chroma_search(collection, query)
        chroma_time = time.perf_counter() - start
        print(f"Chroma HNSW query:  {chroma_time*1000:.3f} ms  | top match id={chroma_ids[0]} dist={chroma_dists[0]:.4f}")

        speedup = bf_time / chroma_time if chroma_time > 0 else float("inf")
        print(f"--> Chroma query was {speedup:.1f}x {'faster' if speedup > 1 else 'slower'} than brute-force")


if __name__ == "__main__":
    run_benchmark()
