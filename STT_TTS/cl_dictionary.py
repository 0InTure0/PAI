from bs4 import BeautifulSoup
import requests


def dic_cl(dic_input):
  query = dic_input + " 뜻"
  res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+query)
  global soup, cl_word, cl_meaning
  soup = BeautifulSoup(res.text, 'html.parser')
  cl_word = soup.find('mark')
  cl_meaning = soup.find('p','api_txt_lines')
  print(cl_word.text)
  print(cl_meaning.text)


dic_cl("마우스")
