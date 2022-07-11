from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import localtime, time
import random
reminder_dic = {999999999999999: 999999999999999}
tm = localtime(time())


city_list = ['서울','경기','수원','대전','부산','울산','전라북도','전라남도','강원도','용인','의정부',
        '강남구', '서초구','송파구','금천구','관악구','구로구','노원구','도봉구','강북구',
        '당산','여의도','목동','마용성','용산수','성동구','구리시','미사','다산','남양주시',
        '가평군','광교','판교','과천','성남','안산','시흥','성남','화성','오산','안산','시흥',
        '송넘','양주시','양주시','동두천','대구','광주','경상남도','대구','경상북도','경북','경남',
        '청주','세종','강원도','철원군','화천군','강원','영구군','인제군','여수','여수시','순천',
        '광양','목포','무안','신안','전주','군산','익산','완주','무주','장수','마포']

#리스트에서 지역 찾기
def find_city(strmsg):
  for j in city_list:                               #지역 리스트
    if( j in strmsg):
      city_input = j
      break
    city_input = "서울시 노원구"                     #기본 지역값
  return city_input

#네이버 기상청 링크 연결, 데이터 불러오기
def cl_city_weather(city_input):
  query = city_input + "+날씨"
  res = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=1&query='+query+'&oquery='+query)
  global soup, cl_weather, cl_time, cl_this_weather, cl_this_temp, cl_this_weather_txt, cl_highest, cl_lowest, cl_tom_weather, cl_tom_temp
  soup = BeautifulSoup(res.text, 'html.parser')
  cl_weather = soup.find_all('span','blind')              #시간별 날씨
  cl_time = soup.find_all('dt','time')                    #날씨의 시간
  cl_lowest = soup.find('span','lowest')                  #오늘 최저기온
  cl_highest = soup.find('span','highest')                #오늘 최고기온
  cl_this_weather = soup.find('span','weather')           #현재 날씨
  cl_this_temp = soup.find('div','temperature_text')      #현재 온도
  cl_tom_weather = soup.find_all('p','summary')           #내일 날씨
  cl_tom_temp = soup.find_all('strong')                   #내일 온도
  cl_this_weather_txt = cl_this_weather.text              #현재 온도 텍스트 값으로 변환

#10시간 이내 눈 또는 비가 오는지 체크
def cl_10h_rain_snowing():
  for i in range(10):
    this_time = cl_time[i].text
    this_weather = cl_weather[i+5].text
    if(list(this_time)[0] == '0'):
      this_time = list(this_time)[1] + '시'
    elif(this_time == '내일'):
      this_time = '24 시'
    if(this_weather == "비"):
      print(this_time, "부터 비가 올 예정입니다. 외출시 우산을 챙겨주세요")
      break
    elif(this_weather == "눈"):
      print(this_time, "부터 눈이 올 예정입니다. 외출시 우산을 챙겨주세요")
      break

#현재 날씨를 확인하고 알려줌
def cl_Weather():
  if(cl_this_weather_txt == "비"):
    print("비가 오고 있습니다. 외출시 우산을 챙겨주세요")
  elif(cl_this_weather_txt == "흐리고 가끔 비"):
    print("흐린 날씨에 가끔 비가 올 것입니다. 외출시 우산을 챙겨주세요")
  elif(cl_this_weather_txt == "눈"):
    print("눈이 오고 있습니다. 외출시 우산을 챙겨주세요")
  else:
    cl_10h_rain_snowing()

#현재 온도를 확인하고 어느정도 더위인지 알려줌
def cl_Temp():
  lowTemp_list = list(cl_lowest.text)
  highTemp_list = list(cl_highest.text)
  string_lowtemp = "".join(lowTemp_list[4:6])
  string_hightemp = "".join(highTemp_list[4:6])
  float_lowtemp = float(string_lowtemp)
  float_hightemp = float(string_hightemp)
  print(cl_lowest.text, cl_highest.text+'입니다.')
  if(float_hightemp >= 26):
    print("매우 더운 날씨네요. 더위 조심하세요")
  if(18 >= float_lowtemp >= 13):
    print("약간 쌀쌀한 날씨네요. 나갈 때 따뜻하게 입어야 겠어요.")
  if(float_lowtemp <= 12):
    print("매우 추운 날씨네요. 감기 조심하세요")

#오늘 날씨에 대한 크롤링을 전체적으로 함
def weather_cl_all(city_input):
  cl_city_weather(city_input)
  print(city_input+"의 현재 날씨는", cl_this_weather_txt, end='')
  cl_Temp()
  cl_Weather()

#내일 날씨, 오전 온도, 오후 온도를 알려줌
def cl_tomorrow(city_input):
  tom_temp_list = list(cl_tom_temp[27].text)
  string_tom_temp = "".join(tom_temp_list[5:7])
  tom_weather = cl_tom_weather[1].text                              #내일 날씨
  speak_tom_weather = "내일 " + city_input + "의 온도는 "+ string_tom_temp+ "도 날씨는 " + tom_weather+"입니다."
  print(speak_tom_weather)

#사전에서 단어 찾기
def cl_dictionary(dic_input):
  query = dic_input + " 뜻"
  res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+query)
  global soup, cl_word, cl_meaning
  soup = BeautifulSoup(res.text, 'html.parser')
  try:
    cl_word = soup.find('mark')
    cl_meaning = soup.find('p','api_txt_lines')
    print(cl_word.text+"의 뜻은 "+cl_meaning.text)
  except:
    print("그 단어는 없는 단어인 것 같습니다.")

#검색할 단어 찾기
def search_word(strmsg):
  mean1 = strmsg.find("가")
  mean2 = strmsg.find("이")
  mean3 = strmsg.find("뜻")
  mean4 = strmsg.find("뭐야")
  strmsg_list = list(strmsg)
  if (mean1 > 1):
    word  = "".join(strmsg_list[:mean1])
  elif (mean3 > mean2 and mean2 > 1):
    word  = "".join(strmsg_list[:mean2])
  elif not(mean3 == -1):
    word  = "".join(strmsg_list[:mean3])
  elif not(mean4 == -1):
    word  = "".join(strmsg_list[:mean4])
  cl_dictionary(word)

#유튜브 재생
def youtube_play(strmsg):
  youtube_find = strmsg.find("유튜브")
  play_find = strmsg.find("틀어줘")
  search_word  = "".join(list(strmsg)[youtube_find+3:play_find])
  email = "minchul90172@gmail.com\n"
  password = "hyunsu0223\n"
  driver = uc.Chrome(use_subprocess=True)
  wait = WebDriverWait(driver, 20)
  url = 'https://accounts.google.com/ServiceLogin/signinchooser?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
  driver.get(url)
  wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
  wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
  wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ytd-searchbox"))).send_keys(search_word)
  wait.until(EC.visibility_of_element_located((By.ID, "search-icon-legacy"))).click()
  wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img"))).click()
  wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ytp-fullscreen-button"))).click()
  while True:
    str2 = input("유튜브 끌까요?: ")  #음성인식 함수 집어넣고 꺼줘라는 말이 인식 될 때까지 반복
    pass
    if("유튜브 꺼" in str2 or "꺼" in str2):
      break

#문자열에서 시간 찾아서 수열로 변환, 현재시간을 수열로 변환
def string_to_time(strmsg, list_msg):
  #시간 단위의 위치 찾기
  year_find = strmsg.find("년")
  mon_find = strmsg.find("월")
  day_find = strmsg.find("일")
  hour_find = strmsg.find("시")
  min_find = strmsg.find("분")
  sec_find = strmsg.find("초")
  #현재시간과 저장하는 타임을 리스트 형태로 저장
  real_time_list = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec]
  time_set_list = [year_find, mon_find, day_find, hour_find, min_find, sec_find]
  time_count = 5
  msg_time = 0
  #빅스비 = 시간이라는 말이 있거나 분만 있을 경우 몇 time 뒤로 인식
  for idx, val in enumerate(time_set_list):
    if not(val == -1):
      list_to_str = "".join(list_msg[val-2:val])
      if(idx == 3 and list_msg[val+1] == "간"):
        int_msg = int(list_to_str)
        int1 = (tm.tm_hour+int_msg)*(10**(2*time_count))
        if(int1 >= 240000):
          int1 = int1 + 760000
        msg_time = msg_time + int1
      elif(idx == 3 and tm.tm_hour > 12):
        int_msg = int(list_to_str)
        int1 = (int_msg+12)*(10**(2*time_count))
        msg_time = msg_time + int1
      elif(idx == 2 and "내일" in strmsg):
        msg_time = msg_time + (tm.tm_mday*1000000)
      elif(idx == 4 and "뒤" in list_msg[min_find:min_find+5]):
        int_msg = int(list_to_str)
        int1 = (tm.tm_min+int_msg)*(10**(2*time_count))
        if(int1 >= 6000):
          int1 = int1 +4000
        msg_time = msg_time + int1
      else:
        int_msg = int(list_to_str)
        int1 = int_msg*(10**(2*time_count))
        msg_time = msg_time + int1
      msg_start = val
    else:
      #년부터 분까지의 시간중 문자열에 없는 경우 리얼타임의 값을 넣음
      if not(idx == 5):
        int1 = real_time_list[idx]*(10**(2*time_count))
        msg_time = msg_time + int1
    time_count = time_count-1
  real_time_count = 5
  real_time_int = 0
  for i in real_time_list:
    int2 = i*(10**(2*real_time_count))
    real_time_int = real_time_int + int2
    real_time_count = real_time_count-1
  if("내일" in strmsg):
    msg_time = msg_time + 1000000
  elif("모레" in strmsg):
    msg_time = msg_time + 2000000
  elif("글피" in strmsg):
    msg_time = msg_time + 3000000
  elif("그글피" in strmsg):
    msg_time = msg_time + 4000000
  if("뒤" in strmsg):
    if("하루" in strmsg):
      msg_time = msg_time + 1000000
    if("이틀" in strmsg):
      msg_time = msg_time + 2000000
    if("사흘" in strmsg):
      msg_time = msg_time + 3000000
    if("나흘" in strmsg):
      msg_time = msg_time + 4000000
  return msg_time, real_time_int, msg_start

#리마인더의 문자 또는 알람의 시간을 딕셔너리로 저장
def reminder_save(strmsg):
  list_msg = list(strmsg)
  msg_time, real_time_int, msg_start = string_to_time(strmsg, list_msg)
  if(list_msg[msg_start+1] == "에"):
    msg_start = msg_start+1
  if(list_msg[msg_start+1] == " " or list_msg[msg_start+2] == " "):
    msg_start = msg_start+1
  remind_msg = "".join(list_msg[msg_start+1:])
  if ("알람" in remind_msg):
    reminder_dic[msg_time] = "알람"
  else:
    reminder_dic[msg_time] = remind_msg
  print("리마인더를 저장 하였습니다.")
  return real_time_int

#딕셔너리 내에 있는 키값을 현재시간과 비교하여 시간이 지나면 알림을 보냄
def reminder_play():
  real_time_list = [tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec]
  real_time_count = 5
  real_time_int = 0
  for i in real_time_list:
    int2 = i*(10**(2*real_time_count))
    real_time_int = real_time_int + int2
    real_time_count = real_time_count-1 
  for k in reminder_dic.keys():
    if(real_time_int >= k):
      if(reminder_dic[k] == "알람"):
        print("알람소리 띠리링띠리링")
      else:
        print("리마인더 알림입니다. ", end='')
        print(reminder_dic[k])
    reminder_d = {key: value for key, value in reminder_dic.items() if not real_time_int >= key}
  return reminder_d

#사전에서 단어 찾기
def cl_dictionary_end_talk(dic_input):
  query = dic_input + " 뜻"
  res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+query)
  global soup, cl_word, cl_meaning
  soup = BeautifulSoup(res.text, 'html.parser')
  try:
    cl_word = soup.find('mark')
    cl_meaning = soup.find('p','api_txt_lines')
    if (type(cl_meaning) == type(None)):
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
      while True:
        if(len(strmsg) == 1):
          strmsg = input('단어가 한 글자입니다 다시 입력해주세요:')
        else:
          break
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

#음성 명령 인식
def voice_commend(strmsg):
  if("날씨" in strmsg):
    city_input = find_city(strmsg)
    if("내일" in strmsg):
      cl_city_weather(city_input)
      cl_tomorrow(city_input)
    else:
      weather_cl_all(city_input)
  elif("온도" in strmsg or "몇 도" in strmsg):
    city_input = find_city(strmsg)
    cl_city_weather(city_input)
    cl_Temp()
  elif("지역" in strmsg):
    if("추가" in strmsg):
      list_msg = list(strmsg)
      city_append = "".join(list_msg[5:])
      city_list.append(city_append)
  elif("뜻" in strmsg or "뭐야" in strmsg):
    search_word(strmsg)
  elif("유튜브" in strmsg):
    if("틀어줘" in strmsg):
      youtube_play(strmsg)
  elif("리마인더" in strmsg):
    reminder_save(" "+strmsg)
  elif("알람" in strmsg):
    reminder_save(" "+strmsg)
  elif("끝말잇기" in strmsg):
    if("하자" in strmsg or "한 판" in strmsg or "할래" in strmsg or "할까" in strmsg):
      set_start = input("누구부터 시작할까요?:")
      if("나부터" in set_start or "나" in set_start or "미" in set_start):
        last_start()
      if("너부터" in set_start or "너" in set_start or "유" in set_start or "파이" in set_start):
        first_start()


while True:
  str1 = input("명령을 입력해주세요:")
  voice_commend(str1)
  reminder_dic = reminder_play()

