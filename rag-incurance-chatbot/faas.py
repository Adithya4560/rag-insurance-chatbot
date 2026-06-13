import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')
li=["What is PMSBY?", "What is PMJJBY?", "How can i apply to PMSBY?", "How can i apply to PMJJBY?"]
embeddings = model.encode(li)
query=model.encode(["Compare PMSBY and PMJJBY"])
index=faiss.IndexFlatL2(384)
index.add(np.array(embeddings))
distances,indices=index.search(np.array(query),k=2)
print("Distances:",distances)
print("Indices:",indices)