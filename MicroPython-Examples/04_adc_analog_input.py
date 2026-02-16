"""
Analog Input (ADC) Example for PSoC™ 6 MicroPython

This example demonstrates reading analog voltage using the ADC (Analog-to-Digital Converter).
The PSoC™ 6 has a 12-bit ADC, but MicroPython provides a 16-bit interface.

Hardware Setup:
- Connect an analog sensor or potentiometer to the ADC pin
- Voltage range: 0V to 3.3V (do not exceed 3.3V!)

Pin Configuration:
- Update ADC_PIN to an available ADC-capable pin on your board
- Common ADC pins: P10_0 to P10_7

Typical Use Cases:
- Reading sensor values (temperature, light, moisture, etc.)
- Potentiometer input
- Battery voltage monitoring
"""

from machine import ADC, Pin
import time

# Configuration - Change this to an ADC-capable pin on your board
ADC_PIN = 'P10_0'  # Common ADC pin

# Reference voltage (PSoC™ 6 uses 3.3V)
VREF = 3.3

# Create ADC object
print(f"Initializing ADC on pin {ADC_PIN}")
adc = ADC(Pin(ADC_PIN))

print("ADC reading started. Press Ctrl+C to stop.")
print("Reading format: Raw Value | Voltage")
print("-" * 40)

try:
    while True:
        # Read raw ADC value (0-65535 for 16-bit)
        raw_value = adc.read_u16()
        
        # Convert to voltage (0V to 3.3V)
        voltage = (raw_value / 65535) * VREF
        
        # Display results
        print(f"Raw: {raw_value:5d} | Voltage: {voltage:5.3f}V")
        
        time.sleep(1)  # Read every second
        
except KeyboardInterrupt:
    print("\nStopped by user")

"""
Example Output:
ADC reading started. Press Ctrl+C to stop.
Reading format: Raw Value | Voltage
----------------------------------------
Raw: 32768 | Voltage: 1.650V
Raw: 45000 | Voltage: 2.265V
Raw: 12000 | Voltage: 0.605V
"""
