from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model=SentenceTransformer('all-MiniLM-L6-v2')
li=["What is PMSBY?","What is PMJJBY?","I am very happy to what i am doing today"]
embeddings=model.encode(li)
print(embeddings.shape)
similarity=cosine_similarity([embeddings[0]], [embeddings[1]])
print("PMSBY VS PMJJBY:",similarity)
similarity2=cosine_similarity([embeddings[0]], [embeddings[2]])
print("PMSBY VS Happy:",similarity2)
