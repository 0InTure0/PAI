import random

#메모장에서 단어 불러오기
def txt_to_list():
  with open('Word_list.txt', 'r', encoding='utf8') as f:
    list_file = f.readlines()
  list_file = [line.rstrip('\n') for line in list_file]
  return list_file
all_text_list = txt_to_list()

#단어장 리스트에서 단어 찾기
def find_word(last_word, first_word, choice_word_last):
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
      choice_word_last = list(choice_word)[len(choice_word)-1]
      print(choice_word)
    except:
      choice_word_last = "제가 졌습니다."
      print(choice_word_last)
  else:
    print('잘못된 단어입니다.'+choice_word_last+'로 시작하는 단어를 해주세요')
  return choice_word_last

#끝말잇기 무한반복
def loop_end_talk(choice_word_last):
  while True:
    strmsg = input('단어를 입력해주세요:')
    if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg):
      print("끝말잇기 즐거웠습니다!")
      break
    str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
    last_word = list(str_word)[len(str_word)-1]
    first_word = list(str_word)[0]
    choice_word_last = find_word(last_word, first_word, choice_word_last)
    if(choice_word_last == "제가 졌습니다."):
      break

#PAI가 먼저 시작할 때
def first_start():
  choice_word = random.choice(all_text_list)
  if(len(choice_word) <= 1):
    while True:
      choice_word = random.choice(all_text_list)
      if(len(choice_word) > 1):
        break
  choice_word_last = list(choice_word)[len(choice_word)-1]
  print("그럼 저부터 시작하겠습니다!", choice_word)
  strmsg = input('단어를 입력해주세요:')
  str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
  last_word = list(str_word)[len(str_word)-1]
  first_word = list(str_word)[0]
  Last_Word = find_word(last_word, first_word, choice_word_last)
  if not (Last_Word == "제가 졌습니다."):
    loop_end_talk(Last_Word)

#PAI가 후에 시작할 떄
def last_start():
  print("먼저 단어를 말씀해주세요!")
  strmsg = input('단어를 입력해주세요:')
  if("졌어" in strmsg or "졌다" in strmsg or "너가 이겼어" in strmsg):
    print("끝말잇기 즐거웠습니다!")
  str_word = ''.join(list(strmsg)[strmsg.rfind(" ")+1:])
  last_word = list(str_word)[len(str_word)-1]
  first_word = list(str_word)[0]
  choice_word_last = find_word(last_word, first_word, first_word)
  if(choice_word_last == "제가 졌습니다."):
    pass
  else:
    loop_end_talk(choice_word_last)

#first_start()
last_start()
