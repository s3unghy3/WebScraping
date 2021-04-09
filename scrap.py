from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://search.naver.com/"
link = "https://search.naver.com/search.naver?where=news&query=sap%20%EC%BD%94%EB%A6%AC%EC%95%84&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=2&ds=&de=&docid=&nso=so%3Ar%2Cp%3A1m%2Ca%3Aall&mynews=0&refresh_start=0&related=0"

req = Request(link, headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(req).read()

with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')

    for item in soup.find_all('a', attrs={'class':'news_tit'}):
        title = item.get('title')
        print(title,end = ' ')
        newslink = item.get('href')
        print(newslink)