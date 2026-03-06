"""
Created by: Jayden Okafor
Created on: Mar 2026
This program turns on the traffic light when the "A" button is clicked
"""

from microbit import *
import neopixel

neopixelStrip = neopixel.NeoPixel(pin16, 4)

# turns off all pixels
neopixelStrip.clear()

# shows happy face
display.show(Image.HAPPY)

# loops so when you click the "A" button again it repeats the sequence
while True:

    # when the a button is pressed
    if button_a.is_pressed():

        # clears the screen
        display.clear()

        # shows checkmark
        display.show(Image.YES)

        # changes the third pixel colour to Green for 1 second
        neopixelStrip[2] = (0, 255, 0)
        neopixelStrip.show()
        sleep(1000)

        # turns off the third pixel and changes the second pixel colour to Yellow for 0.5 seconds
        neopixelStrip[2] = (0, 0, 0)
        neopixelStrip[1] = (255, 255, 0)
        neopixelStrip.show()
        sleep(500)

        # turns off the second pixel and changes the first pixel colour to Red for 1 second
        neopixelStrip[1] = (0, 0, 0)
        neopixelStrip[0] = (255, 0, 0)
        neopixelStrip.show()
        sleep(1000)

        # turns off all pixels
        neopixelStrip.clear()

        # clears the screen
        display.clear()

        # shows happy face
        display.show(Image.HAPPY)
