import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the sensor's OUT pin
SENSOR_PIN = 16

# Set up the GPIO pin as an input
GPIO.setup(SENSOR_PIN, GPIO.IN)


def ir_sensor_callback(channel):
    """Print output when the IR sensor detects an object"""
    if GPIO.input(channel):
        print("Object removed")
    else:
        print("Object detected")


try:
    # Register event handler to handle events from the IR sensor
    GPIO.add_event_detect(SENSOR_PIN, GPIO.BOTH, callback=ir_sensor_callback, bouncetime=500)

    print("IR Sensor Active. Waiting for events...")

    # This loop exists to prevent program termination during
    # standalone testing. The callback itself remains non-blocking
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings when the script is stopped
    GPIO.cleanup()
    print("Program terminated and GPIO cleaned up.")
