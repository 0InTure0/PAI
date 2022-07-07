from bs4 import BeautifulSoup
import requests

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
  cl_lowest = soup.find('span','strong')                  #오늘 최저기온
  cl_highest = soup.find('span','')                       #오늘 최고기온

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
    print("매운 더운 날씨네요. 더위 조심하세요")
  if(18 >= float_lowtemp >= 13):
    print("약간 쌀쌀한 날씨네요. 나갈 때 따뜻하게 입어야 겠어요.")
  if(float_lowtemp <= 12):
    print("매우 추운 날씨네요. 감기 조심하세요")

#오늘 날씨에 대한 크롤링을 전체적으로 함
def weather_cl():
  if("부산" in str1):
    city_input = "부산"
    cl_city_weather(city_input)
    cl_tomorrow()
  else:
    city_input = "서울 노원구"
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

def voice_commend(strmsg):
  if("오늘" in strmsg):
    if("날씨" in strmsg):
      weather_cl()
    elif("온도" in strmsg or "몇 도" in strmsg):
      city_input = "서울"
      cl_city_weather(city_input)
      cl_Temp()
  if("내일" in strmsg):
    if("날씨" in strmsg):
      if("지역" in str1):
        city_input = "부산"
        cl_city_weather(city_input)
        cl_tomorrow()
      else:
        city_input = "서울 노원구"
        cl_city_weather(city_input)
        cl_tomorrow()


str1 = "오늘 서울지역 날씨 어때?"
voice_commend(str1)
