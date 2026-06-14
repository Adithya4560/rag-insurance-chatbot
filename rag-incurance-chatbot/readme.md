# 🏥 Indian Government Schemes RAG Chatbot

A RAG (Retrieval Augmented Generation) based chatbot that provides 
accurate information about Indian government insurance and financial 
schemes using AI.

## 🚀 Live Demo
[Coming Soon - Streamlit Cloud]

## 📌 About The Project
This chatbot helps users get instant, accurate answers about 13 Indian 
government schemes including insurance, pension, housing and savings schemes.
Built using RAG architecture to ensure responses are based on real 
government data, not AI hallucinations.

## 🤖 How It Works
User Question

↓

Convert to Embeddings (Sentence Transformers)

↓

Search Similar Chunks (FAISS Vector DB)

↓

Send Context + Question to Groq LLaMA 3.3

↓
 
Get Answer

## 📋 Schemes Covered
1. Ayushman Bharat Yojana (PMJAY)
2. Pradhan Mantri Jeevan Jyoti Bima Yojana (PMJJBY)
3. Pradhan Mantri Suraksha Bima Yojana (PMSBY)
4. Atal Pension Yojana (APY)
5. Employees State Insurance (ESI)
6. PM Fasal Bima Yojana (PMFBY)
7. National Pension System (NPS)
8. Public Provident Fund (PPF)
9. Sukanya Samriddhi Yojana (SSY)
10. Pradhan Mantri Jan Dhan Yojana (PMJDY)
11. PM Kisan Samman Nidhi (PM-KISAN)
12. PM Shram Yogi Maandhan (PM-SYM)
13. Pradhan Mantri Awas Yojana Urban (PMAY)

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python | Core Language |
| BeautifulSoup | Web Scraping |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| Groq LLaMA 3.3 | Language Model |
| Streamlit | Frontend Interface |

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/Adithya4560/rag-insurance-chatbot.git
cd rag-insurance-chatbot
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```
**4. Run the scraper:**
```bash
python scraper.py
```

**5. Run the app:**
```bash
streamlit run app.py
```

## 💡 Features
- ✅ Answers questions about 13 government schemes
- ✅ Provides official application links
- ✅ Compares schemes on request
- ✅ No hallucination — answers based on real data
- ✅ Clean and intuitive chat interface
- ✅ Custom logo and professional UI

## 📸 Screenshot
[Add screenshot here]

## 🔗 Official Application Portal
For applying to any scheme visit:
**https://www.myscheme.gov.in**

## 👨‍💻 Author
**Adithya Rao**
- GitHub: [@Adithya4560](https://github.com/Adithya4560)
- Email: adithyarao390@gmail.com

## 📄 License
This project is open source and available under the MIT License.