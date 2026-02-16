"""
LED Control with Signal Class for PSoC™ 6 MicroPython

This example demonstrates using the Signal class to handle active-low LEDs.
The Signal class with invert=True automatically handles the inverted logic,
making the code more intuitive.

Supported Boards:
- CY8CPROTO-062-4343W (LED: P13_7)
- CY8CPROTO-063-BLE (LED: P6_3)
- CY8CKIT-062-BLE (LED: P13_7)
- CY8CKIT-062-WIFI-BT (LED: P13_7)
- CY8CKIT-062S2-43012 (LED: P13_7)

Note: Update the LED_PIN constant below for your specific board.
"""

from machine import Signal, Pin

# Configuration - Change this to match your board
LED_PIN = 'P13_7'  # Default for most boards

# Initialize pin
pin = Pin(LED_PIN, Pin.OUT)

# The built-in LEDs on PSoC™ 6 are active-low, so invert is set to True
# This means led.on() will set the pin LOW, and led.off() will set it HIGH
led = Signal(pin, invert=True)

# Turn on the LED
led.on()

print(f"LED on pin {LED_PIN} is now ON")
print("The LED will stay on. To turn it off, run led.off() in the REPL")
