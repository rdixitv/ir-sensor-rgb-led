# Raspberry Pi IR Sensor and RGB LED Routines

This directory contains three Python files:

1. `ir_sensor.py`: Reads input from an IR sensor, uses GPIO event detection and prints messages when an object is detected or removed

2. `rgb_led.py`: Contains functions for controlling an RGB LED, handling the GPIO setup as well

3. `rgb_led_test.py`: Test program for rgb_led.py. It takes keyboard input (r, g, b) to turn on LED colours using the functions from rgb_led.py

## Hardware Requirements
- Raspberry Pi 5
- IR obstacle sensor
- RGB LED
- 3 resistors (220 ohm)
- Breadboard and jumper wires

## Wiring Instructions
### IR Sensor Routine
| IR Sensor Pin | Raspberry Pi Pin                       |
|---------------|----------------------------------------|
| VCC           | 3.3V (pin 1) or 5V (pin 2, 4)          |
| GND           | GND (pin 6, 9, 14, 20, 25, 30, 34, 39) |
| OUT           | GPIO 16 (pin 36)                       |

The wiring is shown in `demonstration/IRSensorConnection.jpg`.

### RGB LED Routine
| LED Pin     | Raspberry Pi Pin |
|-------------|------------------|
| Red Anode   | GPIO 23 (pin 15) |
| Green Anode | GPIO 24 (pin 18) |
| Blue Anode  | GPIO 25 (pin 22) |
| Cathode     | GND              |

Each anode must be connected through a 220 ohm resistor.

The wiring is shown in `demonstration/RGBLEDBreadboardSetup.jpg`.

## Software Requirements
- Python 3
- RPi module (preinstalled)

## How to Run
### 1. IR Sensor Routine

To run:

``` sh
python ir_sensor.py
```

Expected behaviour:

- Prints "Object detected" when an object is placed in front of the sensor
- Prints "Object removed" when the object is taken away
- Stops with `Ctrl + C`

Demonstrated in `demonstration/IRSensorDemonstration.mp4`

### 2. RGB LED Routine

To run:

``` sh
python rgb_led_test.py
```

Expected behaviour:

- Type `r` -> Red LED turns on
- Type `g` -> Green LED turns on
- Type `b` -> Blue LED turns on
- Any other key -> Exit program

Demonstrated in `demonstration/RGBLEDDemonstration.mp4`

Relevant functions:

- turn_on_led(color: Color)
