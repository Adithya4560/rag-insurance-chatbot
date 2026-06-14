from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  
client=Groq(api_key=os.getenv("GROQ_API_KEY"))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "dat", "insurance.txt")

with open(FILE_PATH, "r", encoding="utf-8") as f:
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
    comparison_keywords = [
    "difference",
    "compare",
    "comparison",
    "vs",
    "versus"
    "similarities",
    "dissimilarities"
    ]

    is_comparison = any(
        keyword in question.lower()
        for keyword in comparison_keywords
    )
    scheme_keywords="""1. Ayushman Bharat PMJAY: https://pmjay.gov.in
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
13. Pradhan Mantri Awas Yojana Urban PMAY: https://pmaymis.gov.in/"""
    normal_prompt =f"""
You are an insurance assistant.
{scheme_keywords}
If user asks how to apply or where to apply, provide the relevant link above.
Answer normally using headings, bullet points and paragraphs.

Do not use markdown tables unless the user explicitly asks for a comparison.
"""
    comparison_prompt = f"""
    You are an insurance assistant.
    {scheme_keywords}
    If user asks how to apply or where to apply, provide the relevant link above.
    For comparison questions:

    Return a valid markdown table.

    Example:

    | Feature | APY | PMSBY |
    |----------|----------|----------|
    | Purpose | Pension | Accident Insurance |
    | Age | 18-40 | 18-70 |

    After the table provide a short summary.
    """
    system_prompt = comparison_prompt if is_comparison else normal_prompt

    if is_comparison:
        ind = search(question, k=6)
    else:
        ind = search(question, k=3)
    context="\n".join(ind)
    response=client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role":"system","content":system_prompt},
              {"role":"user","content":f"Context:{context}\n\nQuestions:{question}"}
              ]
)
    return response.choices[0].message.content

