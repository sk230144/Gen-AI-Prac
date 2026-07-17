import chromadb
from sentences import get_all_sentences
from embedd import embeded_function

# Creates a Chroma client. In-memory only (data disappears when the script ends) —
# fine for this experiment, no separate database server needed.
client = chromadb.Client();

# Gets (or creates, if it doesn't exist yet) a named "collection" — think of this
# like a table, but for vectors instead of rows of columns.
collection = client.get_or_create_collection(name = "my_sentence")

# Loads our 100 sentences + topic labels from sentences.py.
sentences, label = get_all_sentences()
# Embeds all 100 sentences into 384-dim vectors using our local model.
embedding = embeded_function(sentences)

# Inserts all 100 vectors into Chroma. This is the moment Chroma builds its
# internal HNSW index — every vector becomes a node wired to its approximate
# neighbors, which is why this step has real time cost (index-build time).
collection.add(
    ids=[str(i) for i in range(len(sentences))],
    embeddings=embedding.tolist(),
)

# A brand-new query sentence, not part of the original 100.
query = "best places to visit on a vacation"
# Embeds just the query the same way (wrap in list, then unwrap the single result).
query_embedding = embeded_function([query])[0]

# Asks Chroma for the 5 nearest vectors to our query — this is where Chroma's
# HNSW graph traversal happens internally (we never see the graph, Chroma
# manages it), instead of comparing against all 100 vectors one by one.
result = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=5,
)
# result contains matched ids, distances (lower = more similar), and other fields.
print(result)