// Phi_PublisherBasic.ino
#include <ESP8266WiFi.h>                 //와이파이 연결용 라이브러리를 불러옴
#include <PubSubClient.h>                //MQTT용 라이브러리를 불러옴
const char* ssid = "MyHome_2G";          //와이파이 이름
const char* password = "lovejy0101!";    //와이파이 비밀번호
const char* userId = "hyunsu";           //유저 아이디
const char* userPw = "040831";           //유저 비밀번호(브로커)
const char* clientId = userId;           //클라이언트 아이디 = 유저 아이디
char* topic = "Smart/Myhome/IOT/LampSwitch/workplace/#";      //sub_pub 할 때 사용할 토픽명
char* server = "192.168.45.197";         //MQTT broker IP 메인 컴퓨터의 어드래스
char messageBuf[100];                    //메시지를 받기 위해 길이 선언
int switch_state = 0;
int on_btn = D2;
int off_btn = D3;
int Relay = D4;

void callback(char* topic, byte* payload, unsigned int length) {    //콜백 함수로 토픽의 이름, 들어오는 값, 값의 길이를 받음
  Serial.println("Message arrived!\nTtopic: " + String(topic));     //토픽명을 출력
  Serial.println("Length: "+ String(length, DEC));                  //문자열의 길이를 출력
  strncpy(messageBuf, (char*)payload, length);                      //messageBuf안에 토픽으로 들어오는 값(payload)을 값의 길이만큼 집어넣음
  messageBuf[length] = '\0';                                        //문자열의 길이 끝에 '\0'(null)을 넣어 문자열의 끝을 알려줌
  String strmsg = String(messageBuf);                               //messageBuf를 아두이노의 string으로 선언
  if(String(topic) == "Smart/Myhome/IOT/LampSwitch/workplace"){     //없애고 테스트 해보기
    digitalWrite(Relay, strmsg.toInt());
  }
  Serial.println(strmsg.toInt());
}

WiFiClient wifiClient; 
PubSubClient client(server, 1883, callback, wifiClient);

void setup() {
  pinMode(on_btn, INPUT_PULLUP);
  pinMode(off_btn, INPUT_PULLUP);
  pinMode(Relay, OUTPUT);
  Serial.begin(9600);
  Serial.print("\nConnecting to ");
  Serial.println(ssid);                                         //연결할 와이파이 명 출력
  WiFi.begin(ssid, password);                                   //와이파이 연결
  while (WiFi.status() != WL_CONNECTED) {                       //와이파이가 연결되지 않았으면 0.5초마다 .을 출력
    Serial.print(".");   delay(500);
  }
  Serial.println("\nWiFi Connected");                           //와이파이가 연결 되었으면 연결되었다고 표시
  while ( !client.connect(clientId, userId, userPw) ){          //메인 클라이언트에 연결
    Serial.print("*");    delay(1000);
  }
  Serial.println("\nConnected to broker");
  Serial.println(String("Subscribing! topic = ") + topic);      //서브크라이브할 토픽 표시
  client.subscribe(topic);
 }

void Pub_msg(int pub_value){
  char buf[10];
  String switch_value =  String(pub_value);
  switch_value.toCharArray(buf, switch_value.length());
  client.publish(topic, buf);
  Serial.println(String(topic) + " : " + buf);
}

void loop() {
  client.loop();  //client라는 변수를 계속 반복함(callback함수 반복)
  if(digitalRead(on_btn) == HIGH){
    digitalWrite(Relay, HIGH);
    Pub_msg(1);
    delay(100);
  }
  else if(digitalRead(off_btn) == HIGH){
    digitalWrite(Relay, LOW);
    Pub_msg(0);
    delay(100);
  }
  delay(100);
 }
