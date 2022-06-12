#참고링크 https://luigibox.tistory.com/76
#실행전 sudo pigpiod
#실행이 끝나고 sudo killall pigpiod
import pigpio
from time import sleep

pi = pigpio.pi() 

def servo(pin, angle):
  oldrange = (180 - 0)
  newrange = (2500 - 500)
  newvalue = (((angle - 0) * newrange)/oldrange)+500           #숫자 범위 변환 코드
  pi.set_servo_pulsewidth(pin, newvalue)                       #지터링 방

while True:
  servo(23, 5)
  servo(24, 5)
  sleep(1)

  servo(23, 175)
  servo(24, 175)
  sleep(1)
