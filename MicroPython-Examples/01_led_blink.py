"""
LED Blink Example for PSoC™ 6 MicroPython

This example demonstrates basic GPIO control by blinking the onboard LED.
The LED toggles on and off every second.

Supported Boards:
- CY8CPROTO-062-4343W (LED: P13_7)
- CY8CPROTO-063-BLE (LED: P6_3)
- CY8CKIT-062-BLE (LED: P13_7)
- CY8CKIT-062-WIFI-BT (LED: P13_7)
- CY8CKIT-062S2-43012 (LED: P13_7)

Note: Update the LED_PIN constant below for your specific board.
"""

from machine import Pin
import time

# Configuration - Change this to match your board
LED_PIN = 'P13_7'  # Default for most boards

# Initialize LED pin as output
led = Pin(LED_PIN, Pin.OUT)

# Start with LED off (HIGH for active-low LED)
led.off()

print("LED Blink started. Press Ctrl+C to stop.")

try:
    while True:
        time.sleep_ms(1000)  # Wait 1 second
        led.toggle()         # Toggle LED state
        
except KeyboardInterrupt:
    print("\nStopped by user")
    led.off()  # Turn off LED when exiting
