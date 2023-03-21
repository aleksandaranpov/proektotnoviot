import requests
import re
from cleanco import basename

for brojac in range(1,50):
    response =requests.get("http://127.0.0.1:5000/companies/{}".format(brojac))
    print(response)
    companies= response.json()["companies"][0]
    cleaned_companies={}
    print(companies)
    name=re.sub(pattern="[^\w\s]",
                repl="",
                string = companies["name"])
    name =re.sub(r"LIMITED","", name)
    name=basename(name)
    name = name.title()
    print(name)
    cleaned_companies={
        name: {"id":companies["id"],
               "country_iso":companies["country_iso"],
                  "city": companies["city"],
                  "nace": companies["nace"],
                  "webesite":companies["website"]
                  }

        }
    print(cleaned_companies)
    response =requests.post("http://127.0.0.1:5000/companies/", json=cleaned_companies)
