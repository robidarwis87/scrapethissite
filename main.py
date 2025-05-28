import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.scrapethissite.com/pages/simple/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

country_block = soup.find_all("div", {"class": "col-md-4 country"})


result = []
for block in country_block:
   name_element = block.find("h3", class_="country-name").get_text(strip=True)
   capital_element = block.find("span", class_="country-capital").get_text(strip=True)
   population_element = block.find("span", class_="country-population").get_text(strip=True)
   area_element = block.find("span", class_="country-area").get_text(strip=True)
   result.append({"name": name_element, "capital": capital_element, "population": population_element, "area": area_element})  

# for item in result:
#    print(f"Country: {item['name']}, Capital: {item['capital']}, Population: {item['population']}, Area: {item['area']}")

with open("result.csv", "w", newline="") as file:
   writer = csv.DictWriter(file, fieldnames=["name", "capital", "population", "area"])
   writer.writeheader()
   writer.writerows(result)