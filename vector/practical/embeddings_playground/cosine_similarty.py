import numpy as np
from sentences import get_all_sentences
from embedd import embeded_function



def cosine_similarity(a, b):
    return np.dot(a, b)




if __name__ == "__main__":
    sentences, label = get_all_sentences()
    embedding = embeded_function(sentences)
    
    sim_similarity = cosine_similarity(embedding[0], embedding[3]);
    print(sentences[0])
    print(sentences[3])
    print("similarity:", sim_similarity)