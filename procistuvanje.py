import requests
import re

response =requests.get("http://127.0.0.1:5000/companies")
companies= response.json()["companies"]
cleaned_companies={}
for company in companies:
    re.sub(pattern="[^\w\s]",
           repl="",
           string = company["name"])
    name =re.sub(r"LIMITED","", company["name"])
    name =re.sub(r"LTD","", company["name"])

    name = name.title()

    cleaned_companies={
        name: {"country_iso":company["country_iso"],
              "city": company["city"],
              "nace": company["nace"],
              "webesite":company["website"]
              }

    }
    print(cleaned_companies)
    response =requests.post("http://127.0.0.1:5000/companies", json=cleaned_companies)



