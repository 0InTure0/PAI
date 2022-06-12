#참고링크 https://makemonument.tistory.com/120
from rpi_ws281x import PixelStrip, Color
import time

LEDCOUNT = 16       # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True       # Invert required when using inverting buffer
BRIGHTNESS = 255

strip = PixelStrip(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS) # Intialize the library (must be called once before other functions).
strip.begin()


for i in range(0,8):
    strip.setPixelColor(i, Color(0,255,0))
    strip.setPixelColor(15-i, Color(0,255,0))
    strip.show()
    time.sleep(0.1)

for j in range(0,8):
    strip.setPixelColor(j, Color(255,255,255))
    strip.setPixelColor(15-j, Color(255,255,255))
    strip.show()
    time.sleep(0.1)
