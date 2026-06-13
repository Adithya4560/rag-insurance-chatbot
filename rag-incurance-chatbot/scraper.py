import requests 
import bs4 as beautifulsoup4

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
url={
    "Ayushman Bharat Yojana PMJAY": "https://en.wikipedia.org/wiki/Ayushman_Bharat_Yojana",
    "Pradhan Mantri Jeevan Jyoti Bima Yojana PMJJBY": "https://en.wikipedia.org/wiki/Pradhan_Mantri_Jeevan_Jyoti_Bima_Yojana",
    "Pradhan Mantri Suraksha Bima Yojana PMSBY": "https://en.wikipedia.org/wiki/Pradhan_Mantri_Suraksha_Bima_Yojana",
    "Atal Pension Yojana APY": "https://en.wikipedia.org/wiki/Atal_Pension_Yojana",
    "Employees State Insurance ESI":"https://en.wikipedia.org/wiki/Employees%27_State_Insurance",
    "PM Fasal Bima Yojana PBF": "https://en.wikipedia.org/wiki/Pradhan_Mantri_Fasal_Bima_Yojana",
    "PM Vaya Vandana Yojana PMV": "https://en.wikipedia.org/wiki/Pradhan_Mantri_Matri_Vandana_Yojana",
    "Public Provident Fund PPF": "https://en.wikipedia.org/wiki/Public_Provident_Fund_(India)",
}
for title, i in url.items():
    res=requests.get(i,headers=headers)
    soup=beautifulsoup4.BeautifulSoup(res.text,"html.parser")
    sour=soup.find("div",id="mw-content-text")
    pa=sour.find_all("p")
    with open("insurance.txt","a",encoding="utf-8") as f:
        f.write(f"======{title}=========\n")
        for p in pa:
            if p.text.strip():
                
                f.write(p.text+"\n")