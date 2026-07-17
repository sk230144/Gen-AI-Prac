import numpy as np
from sentences import get_all_sentences
from embedd import embeded_function
from cosine_similarty import cosine_similarity


def search(query, sentences, embeddings, model_encode_fn, top_k=5):
    query_embedding = model_encode_fn([query])[0]
    scores = []
    for vector in embeddings:
        score = cosine_similarity(query_embedding, vector)
        scores.append(score)
    scores = np.array(scores)
    top_indices = np.argsort(scores)[::-1][:top_k]
    results = []
    for i in top_indices:
        results.append((sentences[i], scores[i]))
    return results


if __name__ == "__main__":
    sentences, labels = get_all_sentences()

    embeddings = embeded_function(sentences)

    query = "best places to visit on a vacation"
    results = search(query, sentences, embeddings, embeded_function)

    print(f"Query: {query}\n")
    for sentence, score in results:
        print(f"{score:.3f}  {sentence}")
