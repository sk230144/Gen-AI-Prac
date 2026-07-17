"""
Step 5 — Benchmark: brute-force numpy vs Chroma (HNSW-based vector DB).

Goal: time both search approaches on the SAME 100 real sentence embeddings
and SEE which is faster, connecting back to the theory in vector/4.md
(brute-force breaks at scale, ANN/HNSW exists to avoid that).
"""

import time
import numpy as np
import chromadb

from sentences import get_all_sentences
from embedd import embeded_function

# Loads our 100 sentences + topic labels from sentences.py.
sentences, labels = get_all_sentences()
# Embeds all 100 sentences into 384-dim, normalized vectors.
embeddings = embeded_function(sentences)

# A brand-new query, not part of the original 100 sentences.
query = "best places to visit on a vacation"
# Embed just the query the same way (wrap in list, then unwrap the single row).
query_embedding = embeded_function([query])[0]


# ---------- Brute-force numpy search ----------
# `embeddings` has shape (100, 384). `query_embedding` has shape (384,).
# `embeddings @ query_embedding` is a matrix-vector multiply: it computes the
# dot product of EVERY row against the query, all at once — much faster than
# a Python for-loop, but doing fundamentally the same brute-force comparison
# (checks all 100 vectors, no index, no shortcuts).
start = time.perf_counter()
scores = embeddings @ query_embedding
top_indices = np.argsort(scores)[::-1][:5]   # sort descending, take top 5
brute_force_time = time.perf_counter() - start

print("=== Brute-force numpy ===")
print(f"Time: {brute_force_time * 1000:.4f} ms")
for i in top_indices:
    print(f"  {scores[i]:.3f}  {sentences[i]}")


# ---------- Chroma (HNSW) search ----------
# In-memory Chroma client — no separate database server needed for this test.
client = chromadb.Client()
collection = client.get_or_create_collection(name="benchmark_sentences")

# Insert time is NOT part of the query benchmark — this is where Chroma
# builds its internal HNSW graph (the real "index build cost" from our notes).
start = time.perf_counter()
collection.add(
    ids=[str(i) for i in range(len(sentences))],
    embeddings=embeddings.tolist(),
)
insert_time = time.perf_counter() - start

# This is the part we actually compare against brute-force: querying an
# ALREADY-BUILT index, using HNSW graph traversal instead of checking
# every vector one by one.
start = time.perf_counter()
result = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=5,
)
chroma_time = time.perf_counter() - start

print("\n=== Chroma (HNSW) ===")
print(f"Insert time (index build): {insert_time:.4f} s")
print(f"Query time: {chroma_time * 1000:.4f} ms")
for id_, dist in zip(result["ids"][0], result["distances"][0]):
    print(f"  dist={dist:.3f}  {sentences[int(id_)]}")


# ---------- Compare ----------
print("\n=== Comparison ===")
if chroma_time > 0:
    speedup = brute_force_time / chroma_time
    faster = "Chroma" if speedup > 1 else "Brute-force"
    print(f"{faster} was faster ({speedup:.2f}x)")
print("Note: at only 100 vectors, brute-force is often just as fast or faster —")
print("the real gap only shows up at much larger scale (see vector_db_benchmark.py).")
