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

f = open("새파일.txt", 'w')
for key in ranking:
    data = "{0}{1}{2}\n".format(key, ':', ranking[key])
    f.write(data)
f.close()
