"""
I2C Communication Example for PSoC™ 6 MicroPython

This example demonstrates I2C (Inter-Integrated Circuit) communication,
commonly used for interfacing with sensors, displays, and other peripherals.

I2C Overview:
- Two-wire serial protocol (SDA - data, SCL - clock)
- Master-Slave architecture (PSoC™ 6 acts as master)
- Multiple devices can share the same bus (each has unique address)
- Typical speed: 100 kHz (Standard) or 400 kHz (Fast Mode)

Hardware Setup:
- Connect I2C device's SDA to PSoC™ 6 SDA pin
- Connect I2C device's SCL to PSoC™ 6 SCL pin
- Connect I2C device's GND to PSoC™ 6 GND
- Connect I2C device's VCC to 3.3V (or appropriate voltage)
- Pull-up resistors (4.7kΩ) on SDA and SCL may be required

Common I2C Pins on PSoC™ 6:
- SCL: P6_0, P9_0, P10_0
- SDA: P6_1, P9_1, P10_1
- Check your board's schematic for available pins
"""

from machine import I2C, Pin
import time

# Configuration - Change these to match your board's I2C pins
I2C_ID = 0          # I2C bus number (0, 1, or 2)
SCL_PIN = 'P6_0'    # Clock pin
SDA_PIN = 'P6_1'    # Data pin
I2C_FREQ = 400000   # 400 kHz (Fast Mode)

print("I2C Communication Example")
print(f"Bus: {I2C_ID}, SCL: {SCL_PIN}, SDA: {SDA_PIN}, Freq: {I2C_FREQ} Hz")
print("-" * 50)

# Initialize I2C bus
try:
    i2c = I2C(I2C_ID, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=I2C_FREQ)
    print("I2C initialized successfully")
except Exception as e:
    print(f"Error initializing I2C: {e}")
    raise

# Scan for I2C devices on the bus
print("\nScanning I2C bus...")
devices = i2c.scan()

if devices:
    print(f"Found {len(devices)} device(s):")
    for addr in devices:
        print(f"  - Device at address: 0x{addr:02X} ({addr})")
else:
    print("No I2C devices found")
    print("Check your connections and pull-up resistors")

# Example: Reading from a specific I2C device
# Uncomment and modify the address for your device
DEVICE_ADDR = 0x48  # Example address (common for some temperature sensors)

if DEVICE_ADDR in devices:
    print(f"\nCommunicating with device at 0x{DEVICE_ADDR:02X}")
    
    try:
        # Example 1: Read 2 bytes from the device
        data = i2c.readfrom(DEVICE_ADDR, 2)
        print(f"Read data: {[hex(b) for b in data]}")
        
        # Example 2: Write a byte to the device
        # i2c.writeto(DEVICE_ADDR, bytes([0x01]))
        
        # Example 3: Write to a register and read response
        # register = 0x00
        # i2c.writeto(DEVICE_ADDR, bytes([register]))
        # data = i2c.readfrom(DEVICE_ADDR, 2)
        
    except Exception as e:
        print(f"Communication error: {e}")
else:
    print(f"\nDevice at 0x{DEVICE_ADDR:02X} not found on bus")

"""
Common I2C Device Addresses:
- 0x48-0x4F: Temperature sensors (LM75, TMP102, etc.)
- 0x50-0x57: EEPROMs (AT24C series)
- 0x68-0x69: Real-time clocks (DS1307, DS3231)
- 0x3C-0x3D: OLED displays (SSD1306)
- 0x76-0x77: Barometric pressure sensors (BMP280, BME280)

I2C Functions:
- i2c.scan() - Find all devices on the bus
- i2c.readfrom(addr, n) - Read n bytes from device
- i2c.writeto(addr, buf) - Write buffer to device
- i2c.readfrom_mem(addr, reg, n) - Read from specific register
- i2c.writeto_mem(addr, reg, buf) - Write to specific register
"""
