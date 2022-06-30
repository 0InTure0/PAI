from gtts.tts import gTTS
from playsound import playsound
import urllib
from bs4 import BeautifulSoup
import urllib.request

#네이버 기상청 지역별 링크
city_input = input('city: ') #지역 선택하는 인풋 함수
query = city_input + "+날씨"
res = requests.get('https://search.naver.com/search.naver?display=15&f=&filetype=0&page=1&query='+query+'&oquery='+query)
soup = BeautifulSoup(res.text, 'html.parser')

cl_weather = soup.find_all('span','blind')
cl_time = soup.find_all('dt','time')
cl_this_weather = soup.find('span','weather')
cl_this_temp = soup.find('div','temperature_text')
cl_this_weather_txt = cl_this_weather.text

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



#10시간 이내 비가 오는지 체크
def crawling_10h_rain():
  for i in range(10):
    this_time = cl_time[i].text
    this_weather = cl_weather[i+5].text
    if(this_weather == "비"):
      if(list(this_time)[0] == '0'):
        this_time = list(this_time)[1] + '시'
      elif(this_time == '내일'):
        this_time = '24 시'
      print(this_time, "부터 비가 올 예정입니다. 외출시 우산을 챙겨주세요")
      speak2(this_time, "부터 비가 올 예정입니다. 외출시 우산을 챙겨주세요")
      break

#10시간 이내 눈이 오는지 체크
def crawling_10h_snow():
  for i in range(10):
    this_time = cl_time[i].text
    this_weather = cl_weather[i+5].text
    if(this_weather == "눈"):
      if(list(this_time)[0] == '0'):
        this_time = list(this_time)[1] + '시'
      elif(this_time == '내일'):
        this_time = '24 시'
      print(this_time, "부터 눈이 올 예정입니다. 외출시 우산을 챙겨주세요")
      speak2(this_time, "부터 눈이 올 예정입니다. 외출시 우산을 챙겨주세요")
      break

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
    crawling_10h_rain()
    crawling_10h_snow()

def cl_Temp():
  temp_list = list(cl_this_temp.text)
  string_temp = "".join(temp_list[6:10])
  float_temp = float(string_temp)
  print("온도는", string_temp,"도 입니다.")
  speak3("온도는", string_temp,"도 입니다.")
  if(float_temp >= 25):
    print("오늘은 매우 덥습니다, 더위 조심하세요")
    speak1("오늘은 매우 덥습니다, 더위 조심하세요")
  if(18 >= float_temp >= 16):
    print("오늘은 약간 쌀쌀한 날씨입니다, 감기 조심하세요")
    speak1("오늘은 약간 쌀쌀한 날씨입니다, 감기 조심하세요")
  if(float_temp <= 15):
    print("오늘은 매우 춥습니다, 감기 조심하세요")
    speak1("오늘은 매우 춥습니다, 감기 조심하세요")

print(city_input,"의 현재 날씨는",cl_this_weather_txt, end='')
speak3(city_input,"의 현재 날씨는 ",cl_this_weather_txt)
cl_Temp()
cl_Weather()
