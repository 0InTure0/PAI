from gtts.tts import gTTS
from playsound import playsound
from bs4 import BeautifulSoup
import requests

#TTS 텍스트 음성 변환 _ 텍스트 수에 맞춰 한 문장씩 변환
def speak1(text1):
  text = text1
  tts = gTTS(text=text, lang='ko')
  filename = 'voice.mp3'
  tts.save(filename)
  playsound(filename)

def speak2(text1, text2):
  text = text1 + text2
  tts = gTTS(text=text, lang='ko')
  filename = 'voice.mp3'
  tts.save(filename)
  playsound(filename)

def speak3(text1, text2, text3):
  text = text1 + text2 + text3
  tts = gTTS(text=text, lang='ko')
  filename = 'voice.mp3'
  tts.save(filename)
  playsound(filename)


#네이버 기상청 지역별 링크
def city_weather_cl(city_input):
  query = city_input + "+날씨"
  res = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=1&query='+query+'&oquery='+query)
  global soup, cl_weather, cl_time, cl_this_weather, cl_this_temp, cl_this_weather_txt, cl_highest, cl_lowest
  soup = BeautifulSoup(res.text, 'html.parser')
  cl_weather = soup.find_all('span','blind')              #시간별 날씨
  cl_time = soup.find_all('dt','time')                    #날씨의 시간
  cl_lowest = soup.find('span','lowest')                  #오늘 최저기온
  cl_highest = soup.find('span','highest')                #오늘 최고기온
  cl_this_weather = soup.find('span','weather')           #현재 날씨
  cl_this_temp = soup.find('div','temperature_text')      #현재 온도
  cl_this_weather_txt = cl_this_weather.text              #현재 온도 텍스트 값으로 변환

  print(cl_lowest.text, cl_highest.text)
  speak2(cl_lowest.text, cl_highest.text)


#10시간 이내 눈 또는 비가 오는지 체크
def crawling_10h_rain_snowing():
  for i in range(10):
    this_time = cl_time[i].text
    this_weather = cl_weather[i+5].text
    if(list(this_time)[0] == '0'):
      this_time = list(this_time)[1] + '시'
    elif(this_time == '내일'):
      this_time = '24 시'
    
    if(this_weather == "비"):
      print(this_time, "부터 비가 올 예정입니다. 외출시 우산을 챙겨주세요")
      speak2(this_time, "부터 비가 올 예정입니다. 외출시 우산을 챙겨주세요")
      break
    elif(this_weather == "눈"):
      print(this_time, "부터 눈이 올 예정입니다. 외출시 우산을 챙겨주세요")
      speak2(this_time, "부터 눈이 올 예정입니다. 외출시 우산을 챙겨주세요")
      break

#현재 날씨를 확인하고 알려줌
def cl_Weather():
  if(cl_this_weather_txt == "비"):
    print("비가 오고 있습니다. 외출시 우산을 챙겨주세요")
    speak1("비가 오고 있습니다. 외출시 우산을 챙겨주세요")
  elif(cl_this_weather_txt == "흐리고 가끔 비"):
    print("흐린 날씨에 가끔 비가 올 것입니다. 외출시 우산을 챙겨주세요")
    speak1("흐린 날씨에 가끔 비가 올 것입니다. 외출시 우산을 챙겨주세요")
  elif(cl_this_weather_txt == "눈"):
    print("눈이 오고 있습니다. 외출시 우산을 챙겨주세요")
    speak1("눈이 오고 있습니다. 외출시 우산을 챙겨주세요")
  else:
    crawling_10h_rain_snowing()

#현재 온도를 확인하고 어느정도 더위인지 알려줌
def cl_Temp():
  lowTemp_list = list(cl_lowest.text)
  highTemp_list = list(cl_highest.text)
  string_lowtemp = "".join(lowTemp_list[4:6])
  string_hightemp = "".join(highTemp_list[4:6])
  float_lowtemp = float(string_lowtemp)
  float_hightemp = float(string_hightemp)
  print(cl_lowest.text, cl_highest.text+'입니다.')
  speak3("온도는", string_temp,"도 입니다.")
  if(float_hightemp >= 26):
    print("매운 더운 날씨네요. 더위 조심하세요")
    speak1("매운 더운 날씨네요. 더위 조심하세요")
  if(18 >= float_lowtemp >= 13):
    print("약간 쌀쌀한 날씨네요. 나갈 때 따뜻하게 입어야 겠어요.")
    speak1("약간 쌀쌀한 날씨네요. 나갈 때 따뜻하게 입어야 겠어요.")
  if(float_lowtemp <= 12):
    print("매우 추운 날씨네요. 감기 조심하세요")
    speak1("매우 추운 날씨네요. 감기 조심하세요")


city_input = input('city: ') #지역 선택하는 인풋 함수
city_weather_cl(city_input)
print(city_input+"의 현재 날씨는", cl_this_weather_txt, end='')
speak3(city_input,"의 현재 날씨는 ",cl_this_weather_txt)
cl_Temp()
cl_Weather()
