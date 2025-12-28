import RPi.GPIO as GPIO
from enum import Enum


# Color enum
# The numbers indicate the GPIO pin where the anode corresponding to each color is connected.
# Modify these according to the GPIO pins used in the actual application.
class Color(Enum):
    RED = 23
    GREEN = 24
    BLUE = 25


# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(Color.RED.value, GPIO.OUT)
GPIO.setup(Color.GREEN.value, GPIO.OUT)
GPIO.setup(Color.BLUE.value, GPIO.OUT)


def turn_on(color: Color):
    """Turn on LED based on argument"""
    GPIO.output(color.value, GPIO.HIGH)
    print(f"Turned on {color}")


def turn_off(color: Color):
    """Turn off LED based on argument"""
    GPIO.output(color.value, GPIO.LOW)


def turn_off_all():
    """Turn off all the LED colors"""
    turn_off(Color.RED)
    turn_off(Color.GREEN)
    turn_off(Color.BLUE)


def turn_on_led(color: Color):
    """Turn off all the LED colors and then turn on the given argument"""
    turn_off_all()
    turn_on(color)
