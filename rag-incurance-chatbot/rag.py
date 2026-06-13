from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq
client=Groq(api_key="GROQ_API_KEY")


with open(r"C:\Users\Lenovo\OneDrive\Desktop\A Folder\rag-incurance-chatbot\dat\insurance.txt", "r", encoding="utf-8") as f:
    data=f.read()
chunks=data.split("\n\n")
model=SentenceTransformer('all-MiniLM-L6-v2')
embeddings=model.encode(chunks)
index=faiss.IndexFlatL2(384)
index.add(np.array(embeddings))
def search(query,k=3):
    query=model.encode([query])
    dis,indices=index.search(np.array(query),k)
    return [chunks[int(i)] for i in indices[0]]



def ask(question):
    ind=search(question)
    context="\n".join(ind)
    response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role":"system","content":"""You are a helpful and very intelligent when it comes to insurance related queries and you have access to a database of insurance related information and you can use that information to answer the user's queries. You can also use the search function to search for relevant information in the database and use that information to answer the user's queries.
               Official application links for schemes:
- Ayushman Bharat PMJAY: https://pmjay.gov.in
- PMJJBY (Life Insurance): https://jansuraksha.gov.in
- PMSBY (Accident Insurance): https://jansuraksha.gov.in  
- Atal Pension Yojana: https://npscra.nsdl.co.in
- ESI ESIC: https://esic.gov.in
- PM Fasal Bima Yojana: https://pmfby.gov.in
- PM Vaya Vandana Yojana: https://licindia.in
- PPF Account: https://www.indiapost.gov.in
If user asks how to apply or where to apply, provide the relevant link above.
If user asks to compare schemes, present a clear comparison table.
If you don't know something, say I don't know.
Do not make up information.
If you don't know something say I don't know.
               """},
              {"role":"user","content":f"Context:{context}\n\nQuestions:{question}"}
              ]
)
    return response.choices[0].message.content

