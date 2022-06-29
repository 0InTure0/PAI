#https://itjy2.tistory.com/131

import urllib.request 
import urllib.parse as parse
from bs4 import BeautifulSoup

rssUrl ="https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"


html = urllib.request.urlopen(rssUrl).read()
text=html.decode("utf-8")
soup = BeautifulSoup(text,"xml")

title = soup.rss.channel.title
wf = soup.rss.channel.item.description.body.location

#title = soup.find("title").string #상대경로
#wf = soup.find("city").string   #상대경로

print(wf)