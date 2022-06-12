#참고링크 https://makemonument.tistory.com/120
from rpi_ws281x import PixelStrip, Color
import pigpio
from time import sleep

LEDCOUNT = 16       # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True       # Invert required when using inverting buffer
BRIGHTNESS = 255

strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS) # Intialize the library (must be called once before other functions).
strip.begin()

pi = pigpio.pi() 

def servo(pin, angle):
    oldrange = (180 - 0)
    newrange = (2500 - 500)
    newvalue = (((angle - 0) * newrange)/oldrange)+500           #숫자 범위 변환 코드
    pi.set_servo_pulsewidth(pin, newvalue)                       #지터링 방

for c in range(0,3):
    for i in range(0,8):
        strip.setPixelColor(i, Color(255,0,0))
        strip.setPixelColor(15-i, Color(255,0,0))
        strip.show()
        sleep(0.1)
    
    servo(23, 5)
    servo(24, 5)
    sleep(1)

    servo(23, 175)
    servo(24, 175)
    sleep(1)

    for j in range(0,8):
        strip.setPixelColor(j, Color(255,255,255))
        strip.setPixelColor(15-j, Color(255,255,255))
        strip.show()
        sleep(0.1)