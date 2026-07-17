import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from sentences import get_all_sentences
from embedd import embeded_function


if __name__ == "__main__":
    sentences, labels = get_all_sentences()

    # Embed all 100 sentences into 384-dim vectors.
    embeddings = embeded_function(sentences)

    # PCA compresses 384 dimensions down to 2, trying to keep points
    # that were close in high-dimensional space still close in 2D.
    # fit_transform() both learns the projection and applies it.
    pca = PCA(n_components=2)
    reduced = pca.fit_transform(embeddings)   # shape (100, 2)

    # matplotlib's scatter `c=` needs numbers, not strings like "cooking".
    # So we map each unique topic name to a number (0, 1, 2, 3, 4).
    unique_topics = list(set(labels))
    topic_to_num = {topic: i for i, topic in enumerate(unique_topics)}
    colors = [topic_to_num[label] for label in labels]

    # reduced[:, 0] = all x-values (first column)
    # reduced[:, 1] = all y-values (second column)
    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(reduced[:, 0], reduced[:, 1], c=colors, cmap="tab10")

    # Build a legend mapping colors back to topic names.
    handles = scatter.legend_elements()[0]
    plt.legend(handles, unique_topics, title="Topic")

    plt.title("Sentence Embeddings Reduced to 2D (PCA)")
    plt.xlabel("Component 1")
    plt.ylabel("Component 2")

    plt.savefig("clusters.png")
    print("Saved plot to clusters.png")
