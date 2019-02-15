import urllib.request as req
from bs4 import BeautifulSoup

def readArticleIntro(arName, lang="en"):
    url = 'https://' + lang + '.wikipedia.org/wiki/' + arName
    page = req.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    entry = soup.find("div" ,{ "id" : "bodyContent" })
    return entry.find_all("p")[1].text

def readArticle(arName, lang="en"):
    url = 'https://' + lang + '.wikipedia.org/wiki/' + arName
    page = req.urlopen(url)
    soup = BeautifulSoup(page.read(), "html.parser")
    entry = soup.find("div" ,{ "id" : "bodyContent" })
    return ''.join([x.text for x in entry.find_all("p")])
