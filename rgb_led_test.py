"""
This is a program to test rgb_led.py
This program calls the routines in rgb_led.py
"""

import rgb_led
from rgb_led import Color
import RPi.GPIO as GPIO

try:
    while True:
        color = input("->")

        if color == 'r':
            rgb_led.turn_on_led(Color.RED)
            print("red")

        elif color == 'g':
            rgb_led.turn_on_led(Color.GREEN)
            print("green")

        elif color == 'b':
            rgb_led.turn_on_led(Color.BLUE)
            print("blue")

        else:
            break

    rgb_led.turn_off_all()


except KeyboardInterrupt:
    # Clean up GPIO settings when the script is stopped
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")
