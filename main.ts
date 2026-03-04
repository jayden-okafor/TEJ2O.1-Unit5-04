/* Copyright (c) 202 MTHS All rights reserved
 *
 * Created by: Jayden Okafor
 * Created on: Mar 2026
 * This program turns on the traffic light when the "A" button is clicked
*/

// variables
let neopixelStrip: neopixel.Strip = null

// cleanup
basic.clearScreen()

neopixelStrip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.setPixelColor(3, neopixel.colors(NeoPixelColors.Black))
neopixelStrip.show()

basic.showIcon(IconNames.Happy)

input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showIcon(IconNames.Yes)

    neopixelStrip.setPixelColor(2, neopixel.colors(NeoPixelColors.Green))
    basic.pause(2000)

    neopixelStrip.setPixelColor(1, neopixel.colors(NeoPixelColors.Yellow))
    basic.pause(1000)

    neopixelStrip.setPixelColor(0, neopixel.colors(NeoPixelColors.Red))
    basic.pause(2000)

    neopixelStrip.show()

})