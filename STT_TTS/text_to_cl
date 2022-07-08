from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


city_list = ['서울','경기','수원','대전','부산','울산','전라북도','전라남도','강원도','용인','의정부',
        '강남구', '서초구','송파구','금천구','관악구','구로구','노원구','도봉구','강북구',
        '당산','여의도','목동','마용성','용산수','성동구','구리시','미사','다산','남양주시',
        '가평군','광교','판교','과천','성남','안산','시흥','성남','화성','오산','안산','시흥',
        '송넘','양주시','양주시','동두천','대구','광주','경상남도','대구','경상북도','경북','경남',
        '청주','세종','강원도','철원군','화천군','강원','영구군','인제군','여수','여수시','순천',
        '광양','목포','무안','신안','전주','군산','익산','완주','무주','장수','마포']

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
def cl_tomorrow():
  tom_temp_list = list(cl_tom_temp[27].text)
  string_tom_temp = "".join(tom_temp_list[5:7])
  float_tom_temp = int(string_tom_temp)               #내일 온도
  cl_tom_weather[1].text                              #내일 날씨
  print(float_tom_temp)

#사전에서 단어 찾기
def cl_dictionary(dic_input):
  query = dic_input + " 뜻"
  res = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+query)
  global soup, cl_word, cl_meaning
  soup = BeautifulSoup(res.text, 'html.parser')
  cl_word = soup.find('mark')
  cl_meaning = soup.find('p','api_txt_lines')
  print(cl_word.text+"의 뜻은 "+cl_meaning.text)

#검색할 단어 찾기
def find_word(strmsg):
  mean1 = strmsg.find("가")
  mean2 = strmsg.find("이")
  mean3 = strmsg.find("뜻")
  mean4 = strmsg.find("뭐야")
  strmsg_list = list(strmsg)
  if (mean1 > 1):
    word  = "".join(strmsg_list[:mean1])
  elif (mean3 > mean2):
    if (mean2 > 1):
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
    if("유튜브" in str2):
      if("꺼" in str2):
        break

#리스트에서 지역 찾기
def find_city(strmsg):
  for j in city_list:                               #지역 리스트
    if( j in strmsg):
      city_input = j
      break
    city_input = "서울시 노원구"                     #기본 지역값
  return city_input

#음성 명령 인식
def voice_commend(strmsg):
  if("날씨" in strmsg):
    city_input = find_city(strmsg)
    if("내일" in strmsg):
      cl_city_weather(city_input)
      cl_tomorrow()
    else:
      weather_cl_all(city_input)
  elif("온도" in strmsg or "몇 도" in strmsg):
    city_input = find_city(strmsg)
    cl_city_weather(city_input)
    cl_Temp()

  if("지역" in strmsg):
    if("추가" in strmsg):
      list_msg = list(strmsg)
      city_append = "".join(list_msg[5:])
      city_list.append(city_append)

  if("뜻" in strmsg or "뭐야" in strmsg):
    find_word(strmsg)

  if("유튜브" in strmsg):
    if("틀어줘" in strmsg):
      youtube_play(strmsg)

str1 = "유튜브 잔잔한 음악 틀어줘"
voice_commend(str1)
