"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel

neopixelStrip = neopixel.NeoPixel(pin16, 4)

neopixelStrip.clear()

display.show(Image.HAPPY)

while True:
    
    if button_a.is_pressed():
        display.clear()
        display.show(Image.YES)

        neopixelStrip[2] = (0, 255, 0)
        neopixelStrip.show()
        sleep(1000)

        neopixelStrip[2] = (0, 0, 0)
        neopixelStrip[1] = (255, 255, 0)
        neopixelStrip.show()
        sleep(500)

        neopixelStrip[1] = (0, 0, 0)
        neopixelStrip[0] = (255, 0, 0)
        neopixelStrip.show()
        sleep(1000)

        neopixelStrip.clear()
        display.clear()
        display.show(Image.HAPPY)
