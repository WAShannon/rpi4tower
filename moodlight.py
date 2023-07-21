import board 
import neopixel
import time 
from random import randint


pixels = neopixel.NeoPixel(board.D18, 4)  # D18 means connect to GPIO18 on Raspberry Pi. 4 means 4 leds 

# led on back of OLED driver board, (255, 0 , 0 ) is RGB format of the light, value from 0-255,  (255,0,0) means (red, green, blue) it will turn on the light to red color. (0, 0, 0 ) will turn off the color. 
pixels[0] = (255, 0, 0) 

# led on fan 
pixels[1] = (0, 255, 0) # NO.1 LED turns on fan color to green 
pixels[2] = (255, 0, 0) # NO.2 LED turns on fan color to red
pixels[3] = (0, 0, 255) # NO.3 LED turns on fan color to blue  

# turns off leds on fan
pixels[4] = (0, 0, 0)　 # turns off all leds on fan

# turn off RGB LED on board 
pixels[0].fill((0,0,0))

# while loop
while True:
    for i in range(0, 255):
         np[1] = (randint(0,i), randint(i, 255), randint(i, 255))
         np[2] = (randint(0,i), randint(i, 255), randint(0, i))
         np[3] = (randint(i, 255), randint(0, i), randint(i, 255))
         time.sleep(0.02)
         np[4] = (0, 0, 0)  # turns off all leds
