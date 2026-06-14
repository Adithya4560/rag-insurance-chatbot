from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  
client=Groq(api_key=os.getenv("GROQ_API_KEY"))

with open(os.path.join("dat", "insurance.txt"), "r", encoding="utf-8") as f:
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
1. Ayushman Bharat PMJAY: https://pmjay.gov.in
2. Pradhan Mantri Jeevan Jyoti Bima Yojana PMJJBY: https://jansuraksha.gov.in
3. Pradhan Mantri Suraksha Bima Yojana PMSBY: https://jansuraksha.gov.in
4. Atal Pension Yojana APY: https://www.myscheme.gov.in/schemes/apy
5. Employees State Insurance ESI: https://esic.gov.in
6. PM Fasal Bima Yojana PMFBY: https://pmfby.gov.in
7. National Pension System NPS: https://npstrust.org.in/
8. Public Provident Fund PPF: https://www.indiapost.gov.in
9. Sukanya Samriddhi Yojana: https://www.indiapost.gov.in
10. Pradhan Mantri Jan Dhan Yojana PMJDY: https://pmjdy.gov.in
11. PM Kisan Samman Nidhi PM-KISAN: https://pmkisan.gov.in
12. PM Shram Yogi Maandhan PM-SYM: https://maandhan.in
13. Pradhan Mantri Awas Yojana Urban PMAY: https://pmaymis.gov.in/
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

