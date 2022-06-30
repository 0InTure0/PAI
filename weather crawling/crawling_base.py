from bs4 import BeautifulSoup
import requests

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

def crawling_10h_rain():
    for i in range(10):
        this_time = cl_time[i].text
        this_weather = cl_weather[i+5].text
        if(this_weather == "비"):
            if(list(this_time)[0] == '0'):
                this_time = list(this_time)[1] + '시'
            print(this_time,"부터 비가 올 예정입니다 외출시 우산을 챙겨주세요")
            break

def crawling_10h_snow():
    for i in range(10):
        this_time = cl_time[i].text
        this_weather = cl_weather[i+5].text
        if(this_weather == "눈"):
            if(list(this_time)[0] == '0'):
                this_time = list(this_time)[1] + '시'
            print(this_time,"부터 눈이 올 예정입니다 외출시 우산을 챙겨주세요")
            break

def cl_Weather():
    if(cl_this_weather_txt == "비"):
        print("비가 오고 있습니다. 외출시 우산을 챙겨주세요")
    elif(cl_this_weather_txt == "흐리고 가끔 비"):
        print("흐린 날씨에 가끔 비가 올 것입니다. 외출시 우산을 챙겨주세요")
    elif(cl_this_weather_txt == "눈"):
        print("눈이 오고 있습니다. 외출시 우산을 챙겨주세요")
    else:
        crawling_10h_rain()
        crawling_10h_snow()

def cl_Temp():
    temp_list = list(cl_this_temp.text)
    string_temp = "".join(temp_list[6:10])
    float_temp = float(string_temp)
    print(", 온도는", string_temp,"도 입니다.")
    if(float_temp >= 28):
        print("오늘은 매우 덥습니다, 더위 조심하세요")
    if(float_temp <= 5):
        print("오늘은 매우 춥습니다, 감기 조심하세요")

print("현재 날씨는",cl_this_weather_txt, end='')
cl_Temp()
cl_Weather()
