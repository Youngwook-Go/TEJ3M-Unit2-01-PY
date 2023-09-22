"""
Created by: Youngwook Go
Created on: Sep 2023
Blinks Arduino Pico Built-In LED
"""

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
	led.value = True
	time.sleep(1)
	led.value = False
	time.sleep (1)
