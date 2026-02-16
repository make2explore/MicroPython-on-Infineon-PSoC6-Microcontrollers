"""
Button Input Example for PSoC™ 6 MicroPython

This example demonstrates reading a button input and controlling an LED.
When the button is pressed, the LED turns on. When released, it turns off.

Hardware Setup:
- Connect a push button between the button pin and GND
- The internal pull-up resistor is enabled, so no external resistor is needed
- Most PSoC™ 6 boards have onboard buttons you can use

Pin Configuration:
- Update BUTTON_PIN to match your board's button pin
- Update LED_PIN to match your board's LED pin

Common Button Pins:
- CY8CPROTO-062-4343W: P0_4 (SW2)
- CY8CKIT-062-BLE: P0_4 (SW2)
- Check your board's schematic for the correct pin
"""

from machine import Pin
import time

# Configuration - Change these to match your board
LED_PIN = 'P13_7'     # LED pin for most boards
BUTTON_PIN = 'P0_4'   # Common button pin (check your board's schematic)

# Configure button pin with internal pull-up
# Button is active-low (pressed = 0, released = 1)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Configure LED pin
led = Pin(LED_PIN, Pin.OUT)
led.off()  # Start with LED off

print(f"Button input example started")
print(f"Button pin: {BUTTON_PIN}, LED pin: {LED_PIN}")
print("Press the button to turn on the LED. Press Ctrl+C to stop.")

try:
    while True:
        if button.value() == 0:  # Button pressed (active-low)
            led.on()
        else:                     # Button released
            led.off()
        
        time.sleep_ms(50)  # Small delay for debouncing
        
except KeyboardInterrupt:
    print("\nStopped by user")
    led.off()  # Turn off LED when exiting
