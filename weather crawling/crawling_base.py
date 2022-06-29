#https://cosyp.tistory.com/240

import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req

now = datetime.datetime.now()
nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 입니다.')

#네이버 날씨 크롤링
# Phase1 Seoul Weather Crawling

webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
soup = BeautifulSoup(webpage, 'html.parser')
this_weather = soup.find_all('span','blind')
this_time = soup.find_all('dt','time')

print(this_time[0].text, end='')
print(this_weather[5].text)
