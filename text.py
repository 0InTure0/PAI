from gtts.tts import gTTS
from playsound import playsound
import urllib
from bs4 import BeautifulSoup
import urllib.request

#네이버 기상청 지역별 링크
city_input = input('city: ') #지역 선택하는 인풋 함수
if(city_input == "서울"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
elif(city_input == "울산"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9A%B8%EC%82%B0+%EB%82%A0%EC%94%A8&')
elif(city_input == "수원"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%88%98%EC%9B%90+%EB%82%A0%EC%94%A8')
elif(city_input == "부산"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_sug.asiw&where=nexearch&query=%EB%B6%80%EC%82%B0+%EB%82%A0%EC%94%A8')
elif(city_input == "대전"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EC%A0%84+%EC%9C%A0%EC%84%B1%EA%B5%AC+%EB%82%A0%EC%94%A8')
elif(city_input == "포항"):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%8F%AC%ED%95%AD+%EB%82%A0%EC%94%A8')

#네이버 기상청 크롤링 데이터
soup = BeautifulSoup(webpage, 'html.parser')
cl_weather = soup.find_all('span','blind')
cl_time = soup.find_all('dt','time')
cl_this_weather = soup.find('span','weather')
cl_this_temp = soup.find('div','temperature_text')
cl_this_weather_txt = cl_this_weather.text

#TTS 텍스트 음성 변환

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
            print(this_time, "부터 비가 올 예정입니다 외출시 우산을 챙겨주세요")
            speak2(this_time, "부터 비가 올 예정입니다 외출시 우산을 챙겨주세요")
            break

#10시간 이내 눈이 오는지 체크
def crawling_10h_snow():
    for i in range(10):
        this_time = cl_time[i].text
        this_weather = cl_weather[i+5].text
        if(this_weather == "눈"):
            if(list(this_time)[0] == '0'):
                this_time = list(this_time)[1] + '시'
            print(this_time, "부터 눈이 올 예정입니다 외출시 우산을 챙겨주세요")
            speak2(this_time, "부터 눈이 올 예정입니다 외출시 우산을 챙겨주세요")
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
    if(float_temp >= 28):
        print("오늘은 매우 덥습니다, 더위 조심하세요")
        speak1("오늘은 매우 덥습니다, 더위 조심하세요")
    if(float_temp <= 5):
        print("오늘은 매우 춥습니다, 감기 조심하세요")
        speak1("오늘은 매우 춥습니다, 감기 조심하세요")

print("현재 날씨는",cl_this_weather_txt, end='')
speak2("현재 날씨는",cl_this_weather_txt)

cl_Temp()
cl_Weather()
