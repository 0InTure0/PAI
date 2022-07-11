import random
from types import NoneType
from bs4 import BeautifulSoup
import requests

#사전에서 단어 찾기
def cl_dictionary_end_talk(dic_input):
  query = dic_input + " 뜻"
  res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+query)
  global soup, cl_word, cl_meaning
  soup = BeautifulSoup(res.text, 'html.parser')
  try:
    cl_word = soup.find('mark')
    cl_meaning = soup.find('p','api_txt_lines')
    if (type(cl_meaning) == NoneType):
      word_value = False
      print("그 단어는 없는 단어인 것 같습니다.")
    else:
      word_value = True
  except:
    word_value = False
    print("그 단어는 없는 단어인 것 같습니다.")
  return word_value

#메모장에서 단어 불러오기
def txt_to_list():
  with open('Word_list.txt', 'r', encoding='utf8') as f:
    list_file = f.readlines()
  list_file = [line.rstrip('\n') for line in list_file]
  return list_file
all_text_list = txt_to_list()

#검색한 단어 뜻이 없다면 반복시키기
def search_word_strmsg(strmsg):
  word_value = cl_dictionary_end_talk(strmsg)
  Nesting_Break = True
  while True:
    if(word_value == False):
      strmsg = input("다시 입력해주세요:")
      word_value = cl_dictionary_end_talk(strmsg)
      if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg or "안 해" in strmsg):
        print("끝말잇기 즐거웠습니다!")
        Nesting_Break = False
        break
    else:
      strmsg = strmsg
      Nesting_Break = True
      break
  return strmsg, Nesting_Break

#단어장 리스트에서 단어 찾기
def end_talk_find_word(last_word, first_word, choice_word_last, play_word_list):
  if(first_word == choice_word_last):
    last_word_find_list = []
    for j in all_text_list:
      if(last_word in j):
        if(list(j)[0] == last_word):
          last_word_find_list.append(j)
    try:
      choice_word = random.choice(last_word_find_list)
      if(len(choice_word) <= 1):
        while True:
          choice_word = random.choice(last_word_find_list)
          if(len(choice_word) > 1):
            break
      #중복단어 있는지 찾기
      for W in play_word_list:
        if(W == choice_word):
          choice_word = random.choice(last_word_find_list)
          if(W == choice_word):
            choice_word == 00
        else:
          pass
      play_word_list.append(choice_word)
      choice_word_last = list(choice_word)[len(choice_word)-1]
      print(choice_word)
    except:
      choice_word_last = "제가 졌습니다."
      print(choice_word_last)
  else:
    print('잘못된 단어입니다.'+choice_word_last+'로 시작하는 단어를 해주세요')
  return choice_word_last

#끝말잇기 무한반복
def loop_end_talk(choice_word_last, play_word_list):
  while True:
    Nesting_Break = True
    strmsg = input('단어를 입력해주세요:')
    while True:
      if(len(strmsg) == 1):
        strmsg = input('단어가 한 글자입니다 다시 입력해주세요:')
      else:
        break
    if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg or "안 해" in strmsg):
      print("끝말잇기 즐거웠습니다!")
      break
    strmsg, Nesting_Break = search_word_strmsg(strmsg)
    if(Nesting_Break == False):
      break
    for W in play_word_list:
      if(W == strmsg):
        while True:
          if(W == strmsg):
            strmsg = input("중복되는 단어입니다. 단어를 다시 입력해주세요:")
            if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg or "안 해" in strmsg):
              print("끝말잇기 즐거웠습니다!")
              Nesting_Break = False
              break
      else:
        pass
    if(Nesting_Break == False):
      break
    play_word_list.append(strmsg)
    str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
    last_word = list(str_word)[len(str_word)-1]
    first_word = list(str_word)[0]
    choice_word_last = end_talk_find_word(last_word, first_word, choice_word_last, play_word_list)
    if(choice_word_last == "제가 졌습니다."):
      break

#PAI가 먼저 시작할 때
def first_start():
  play_word_list = []
  choice_word = random.choice(all_text_list)
  if(len(choice_word) <= 1):
    while True:
      choice_word = random.choice(all_text_list)
      if(len(choice_word) > 1):
        break
  choice_word_last = list(choice_word)[len(choice_word)-1]
  print("그럼 저부터 시작하겠습니다!", choice_word)
  play_word_list.append(choice_word)
  strmsg = input('단어를 입력해주세요:')
  while True:
    if(len(strmsg) == 1):
      strmsg = input('단어가 한 글자입니다 다시 입력해주세요:')
    else:
      break
  strmsg, Nesting_Break = search_word_strmsg(strmsg)
  str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
  last_word = list(str_word)[len(str_word)-1]
  first_word = list(str_word)[0]
  play_word_list.append(strmsg)
  Last_Word = end_talk_find_word(last_word, first_word, choice_word_last, play_word_list)
  if not (Last_Word == "제가 졌습니다."):
    loop_end_talk(Last_Word, play_word_list)

#PAI가 후에 시작할 떄
def last_start():
  play_word_list = []
  print("먼저 단어를 말씀해주세요!")
  strmsg = input('단어를 입력해주세요:')
  while True:
    if(len(strmsg) == 1):
      strmsg = input('단어가 한 글자입니다 다시 입력해주세요:')
    else:
      break
  strmsg, Nesting_Break = search_word_strmsg(strmsg)
  if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg or "안 해" in strmsg):
    print("끝말잇기 즐거웠습니다!")
  else:
    play_word_list.append(strmsg)
    str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
    last_word = list(str_word)[len(str_word)-1]
    first_word = list(str_word)[0]
    choice_word_last = end_talk_find_word(last_word, first_word, first_word, play_word_list)
    if(choice_word_last == "제가 졌습니다."):
      pass
    else:
      loop_end_talk(choice_word_last, play_word_list)

#first_start()
last_start()

