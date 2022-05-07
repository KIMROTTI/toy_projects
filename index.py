import requests
from bs4 import BeautifulSoup

req = requests.get("https://issue.zum.com/")
soup = BeautifulSoup(req.text, 'lxml')
ul = soup.find("ul", {"id": "issueKeywordList"})
num = ul.findAll("span", {"class": "num"})
word = ul.findAll("span", {"class": "word"})
ranking = {}

for i, n in enumerate(num):
    ranking[n.text] = word[i].text
print(ranking)
