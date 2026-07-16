import numpy as np
from sentence_transformers import SentenceTransformer
from sentences import get_all_sentences


MODEL_NAME = "all-MiniLM-L6-v2"

def embeded_function(sentences, model = MODEL_NAME):
    model = SentenceTransformer(model)
    embeddings = model.encode(sentences, normalize_embeddings=True)
    return np.array(embeddings)


if __name__ == "__main__":
    sentences, label = get_all_sentences()
    embedding = embeded_function(sentences)
    print(f"Embedding shape: {embedding.shape}")   # (100, 384)