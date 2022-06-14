import paho.mqtt.client as mqtt
from rpi_ws281x import PixelStrip, Color
import pigpio
from time import sleep

LEDCOUNT = 16       # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True       # Invert required when using inverting buffer
BRIGHTNESS = 255

length_servo_pin = 23
width_servo_pin = 24

strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS) # Intialize the library (must be called once before other functions).
strip.begin()

pi = pigpio.pi() 

def servo(pin, angle):
    oldrange = (180 - 0)
    newrange = (2500 - 500)
    newvalue = (((angle - 0) * newrange)/oldrange)+500           #숫자 범위 변환 코드
    pi.set_servo_pulsewidth(pin, newvalue)                       #지터링 없는 서보모터 제어

def on_connect( client, userdata, flags, rc ):
  print("Connect with result code " + str(rc) )  #결과 코드로 연결 str - 연결 결과를 표시해줌
  client.subscribe("Smart/Myhome/#")  #클라이언트가 받는 위치 지정

def on_message( client, userdata, msg ):
  str_msg = str(msg.payload)
  print( msg.topic +" "+str_msg)

  if (msg.topic == "Smart/Myhome/Rasp/Length"):
    int_msg = int(str_msg[2:len(str_msg)-1])
    print("length", int_msg)
    servo(length_servo_pin, int_msg)
  
  if (msg.topic == "Smart/Myhome/Rasp/Width"):
    int_msg = int(str_msg[2:len(str_msg)-1])
    print("width", int_msg)
    servo(width_servo_pin, int_msg)
  
  if (msg.topic == "Smart/Myhome/Rasp/Neopixel"):
    print("Neopixel color")
    int_msg = int(str_msg[2:len(str_msg)-1])
    print("width", int_msg)
    if(int_msg == 1):
      for i in range(0,8):
        strip.setPixelColor(i, Color(255,0,0))
        strip.setPixelColor(15-i, Color(255,0,0))
        strip.show()
        sleep(0.1)
    elif(int_msg == 0):
      for j in range(0,8):
        strip.setPixelColor(j, Color(255,255,255))
        strip.setPixelColor(15-j, Color(255,255,255))
        strip.show()
        sleep(0.1)


client = mqtt.Client( )
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('hyunsu', '0223')
client.connect("localhost", 1883, 60)
client.loop_forever( )