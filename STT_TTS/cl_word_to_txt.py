from bs4 import BeautifulSoup
import requests

def cl_word_list():
  res = requests.get('https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800')
  soup = BeautifulSoup(res.text, 'html.parser')
  cl_word = soup.find_all('dd')

  cl_word_list = []
  word_list = []
  for i in range(5889):
    word = cl_word[i].text
    cl_word_list.append(word)

  for j in cl_word_list:
    if (len(j) > 1):
      list_j = list(j)
      if(not list_j[len(j)-1] == '다' and not "(" in j and not ":" in j):
        word_list.append(j)
    else:
      pass
  
  return word_list

word_list = cl_word_list()

with open('Word_list.txt', 'w', encoding='utf8') as f:
    for line in word_list:
        f.write(line+'\n')
