from bs4 import BeautifulSoup
import requests

    # url of the website you want to scrape
url = ""
    # uses requests library to perform a get request
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
    # finding prices of a certain commodity on a website
prices = doc.find_all(text="$")
prices[0].parent


with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")
print(tags)