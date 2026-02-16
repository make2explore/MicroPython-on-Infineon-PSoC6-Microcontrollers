"""
PWM LED Fade Example for PSoC™ 6 MicroPython

This example demonstrates Pulse Width Modulation (PWM) by creating a smooth
LED fading effect. The LED brightness gradually increases and decreases.

PWM Configuration:
- Frequency: 1000 Hz (1 kHz) - high enough to avoid visible flicker
- Duty Cycle: 0-65535 (16-bit resolution)
  - 0 = 0% duty cycle (LED off)
  - 65535 = 100% duty cycle (LED fully on)

Supported Boards:
- CY8CPROTO-062-4343W (LED: P13_7)
- CY8CPROTO-063-BLE (LED: P6_3)
- CY8CKIT-062-BLE (LED: P13_7)
- CY8CKIT-062-WIFI-BT (LED: P13_7)
- CY8CKIT-062S2-43012 (LED: P13_7)

Note: PWM can be used with any GPIO pin, not just LED pins.
"""

from machine import Pin, PWM
import time

# Configuration - Change this to match your board
LED_PIN = 'P13_7'  # Default for most boards

# PWM Configuration
PWM_FREQ = 1000     # 1 kHz frequency
FADE_STEP = 256     # Step size for smooth fading
FADE_DELAY = 10     # Delay in ms between steps

# Create PWM object on the LED pin
pwm_led = PWM(Pin(LED_PIN))

# Set PWM frequency
pwm_led.freq(PWM_FREQ)

print(f"PWM LED fade example started on pin {LED_PIN}")
print(f"Frequency: {PWM_FREQ} Hz")
print("Press Ctrl+C to stop.")

try:
    while True:
        # Fade in (LED gets brighter)
        for duty in range(0, 65536, FADE_STEP):
            pwm_led.duty_u16(duty)
            time.sleep_ms(FADE_DELAY)
        
        # Fade out (LED gets dimmer)
        for duty in range(65535, -1, -FADE_STEP):
            pwm_led.duty_u16(duty)
            time.sleep_ms(FADE_DELAY)
            
except KeyboardInterrupt:
    print("\nStopped by user")
    pwm_led.deinit()  # Cleanup PWM

"""
PWM Applications:
- LED brightness control
- Motor speed control
- Servo motor positioning
- Audio tone generation
- Power regulation
"""
