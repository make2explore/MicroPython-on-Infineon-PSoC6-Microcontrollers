"""
CY8CKIT-062S2-AI Onboard Sensors Example
PSoC™ 6 AI Evaluation Kit Specific Features

This example demonstrates how to work with the unique sensors available
on the CY8CKIT-062S2-AI board, which is designed for Edge AI and ML applications.

Onboard Sensors:
- BMI270: 6-axis IMU (accelerometer + gyroscope)
- BMM350: 3-axis magnetometer
- DPS368: Barometric pressure sensor
- PDM Microphone: Digital MEMS microphone
- BGT60TR13C: 60GHz RADAR sensor

Note: This board is typically programmed using ModusToolbox and DEEPCRAFT Studio
for AI/ML applications. MicroPython support provides basic I/O and sensor access.

For full AI/ML capabilities, refer to Infineon's DEEPCRAFT Studio documentation.
"""

from machine import I2C, Pin
import time

print("CY8CKIT-062S2-AI Sensor Examples")
print("=" * 60)

# Board-specific pin configuration
# Using board_config.py is recommended for better code portability
LED_PIN = 'P13_7'
BUTTON_PIN = 'P0_4'
I2C_SDA = 'P6_1'
I2C_SCL = 'P6_0'

# Sensor interrupt pins (configured on the board)
IMU_INT_PIN = 'P1_5'      # BMI270 interrupt
MAG_INT_PIN = 'P1_0'      # BMM350 interrupt  
PRESSURE_INT_PIN = 'P1_4' # DPS368 interrupt

# ============================================================================
# Example 1: I2C Bus Scan - Detect Onboard Sensors
# ============================================================================
print("\nExample 1: Scanning I2C bus for onboard sensors...")
print("-" * 60)

try:
    # Initialize I2C (onboard sensors are on I2C0)
    i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=400000)
    
    # Scan for devices
    devices = i2c.scan()
    
    if devices:
        print(f"Found {len(devices)} I2C device(s):")
        
        # Expected sensor addresses on CY8CKIT-062S2-AI:
        sensor_map = {
            0x68: "BMI270 - 6-axis IMU (Accelerometer + Gyroscope)",
            0x69: "BMI270 - 6-axis IMU (Alternative address)",
            0x14: "BMM350 - 3-axis Magnetometer",
            0x77: "DPS368 - Barometric Pressure Sensor",
            0x76: "DPS368 - Barometric Pressure (Alternative address)"
        }
        
        for addr in devices:
            sensor_name = sensor_map.get(addr, "Unknown device")
            print(f"  0x{addr:02X} ({addr:3d}) - {sensor_name}")
    else:
        print("No I2C devices found!")
        print("Check connections and sensor power")
        
except Exception as e:
    print(f"I2C initialization error: {e}")
    print("Note: Sensor drivers may require ModusToolbox libraries")

# ============================================================================
# Example 2: LED and Button (Basic Board Test)
# ============================================================================
print("\n" + "=" * 60)
print("Example 2: Basic board test - LED and Button")
print("-" * 60)

led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

print("Press the button (SW2) to toggle the LED...")
print("Test will run for 10 seconds")

led.off()
start_time = time.time()

while time.time() - start_time < 10:
    if button.value() == 0:  # Button pressed (active low)
        led.on()
        print("  Button pressed - LED ON")
        time.sleep(0.3)  # Debounce
    else:
        led.off()
    time.sleep(0.05)

led.off()
print("Basic board test completed")

# ============================================================================
# Example 3: Interrupt Pin Configuration (for sensor events)
# ============================================================================
print("\n" + "=" * 60)
print("Example 3: Sensor interrupt pin configuration")
print("-" * 60)

# Configure interrupt pins as inputs
imu_int = Pin(IMU_INT_PIN, Pin.IN)
mag_int = Pin(MAG_INT_PIN, Pin.IN)
pressure_int = Pin(PRESSURE_INT_PIN, Pin.IN)

print(f"IMU interrupt pin (P1_5): {imu_int.value()}")
print(f"Magnetometer interrupt pin (P1_0): {mag_int.value()}")
print(f"Pressure sensor interrupt pin (P1_4): {pressure_int.value()}")

print("\nNote: Interrupts require sensor configuration via I2C")
print("Refer to sensor datasheets for interrupt setup details")

# ============================================================================
# Example 4: Reading BMI270 WHO_AM_I Register
# ============================================================================
print("\n" + "=" * 60)
print("Example 4: Reading BMI270 IMU chip ID")
print("-" * 60)

BMI270_ADDR = 0x68  # Default I2C address
BMI270_CHIP_ID_REG = 0x00

try:
    # Read chip ID register
    chip_id_data = i2c.readfrom_mem(BMI270_ADDR, BMI270_CHIP_ID_REG, 1)
    chip_id = chip_id_data[0]
    
    print(f"BMI270 Chip ID: 0x{chip_id:02X}")
    
    if chip_id == 0x24:
        print("✓ BMI270 IMU detected and responding correctly!")
    else:
        print(f"⚠ Unexpected chip ID (expected 0x24, got 0x{chip_id:02X})")
        
except Exception as e:
    print(f"Error reading BMI270: {e}")
    print("Sensor may require initialization or different I2C address")

# ============================================================================
# Example 5: Reading DPS368 Pressure Sensor ID
# ============================================================================
print("\n" + "=" * 60)
print("Example 5: Reading DPS368 Pressure Sensor ID")
print("-" * 60)

DPS368_ADDR = 0x77  # Default I2C address
DPS368_PROD_ID_REG = 0x0D

try:
    # Read product ID register
    prod_id_data = i2c.readfrom_mem(DPS368_ADDR, DPS368_PROD_ID_REG, 1)
    prod_id = prod_id_data[0]
    
    print(f"DPS368 Product ID: 0x{prod_id:02X}")
    
    if prod_id == 0x10:
        print("✓ DPS368 Pressure Sensor detected!")
    else:
        print(f"⚠ Unexpected product ID (expected 0x10)")
        
except Exception as e:
    print(f"Error reading DPS368: {e}")
    # Try alternative address
    try:
        DPS368_ADDR_ALT = 0x76
        prod_id_data = i2c.readfrom_mem(DPS368_ADDR_ALT, DPS368_PROD_ID_REG, 1)
        prod_id = prod_id_data[0]
        print(f"Found at alternative address 0x{DPS368_ADDR_ALT:02X}")
        print(f"DPS368 Product ID: 0x{prod_id:02X}")
    except:
        print("Sensor not responding at either address")

# ============================================================================
# Example 6: Board Information and Capabilities
# ============================================================================
print("\n" + "=" * 60)
print("CY8CKIT-062S2-AI Board Information")
print("=" * 60)

board_info = """
Board: PSoC™ 6 AI Evaluation Kit (CY8CKIT-062S2-AI)
MCU: CY8C624ABZI-S2D44
  - Dual-core: ARM Cortex-M4F @ 150MHz + Cortex-M0+ @ 100MHz
  - Flash: 2 MB
  - SRAM: 1 MB

Wireless:
  - Wi-Fi: 802.11b/g/n (2.4GHz)
  - Bluetooth: 5.2 (BR/EDR/LE)
  - Module: Murata LBEE5KL1YN (CYW43439)

Onboard Sensors:
  - BMI270: 6-axis IMU (Accel + Gyro)
  - BMM350: 3-axis Magnetometer
  - DPS368: Barometric Pressure
  - PDM Microphone: Digital MEMS
  - BGT60TR13C: 60GHz RADAR

Storage:
  - 512 MB Quad-SPI NOR Flash
  - microSD card slot

Connectivity:
  - USB Type-C (programming & power)
  - Arduino headers
  - Pmod connectors

Primary Use Case:
  - Edge AI / Machine Learning
  - Sensor Fusion
  - Motion Detection
  - Audio Classification
  - Presence Detection (RADAR)

Software Ecosystem:
  - ModusToolbox™ (Primary)
  - DEEPCRAFT™ Studio (AI/ML)
  - MicroPython (GPIO & Basic I/O)
"""

print(board_info)

print("\n" + "=" * 60)
print("Important Notes for CY8CKIT-062S2-AI:")
print("=" * 60)

notes = """
1. SENSOR DRIVERS:
   MicroPython provides basic I2C access to sensors.
   For full sensor functionality, use ModusToolbox libraries.

2. AI/ML DEVELOPMENT:
   This board is optimized for AI/ML applications.
   Use DEEPCRAFT Studio (formerly Imagimob Studio) for:
   - Data collection from sensors
   - ML model training
   - Model deployment to PSoC™ 6

3. RADAR SENSOR (BGT60TR13C):
   Requires specialized configuration via SPI.
   Refer to Infineon's RADAR SDK in ModusToolbox.

4. PDM MICROPHONE:
   Audio capture requires PDM-to-PCM conversion.
   ModusToolbox provides audio middleware.

5. WI-FI & BLUETOOTH:
   Network connectivity requires additional firmware.
   MicroPython network support may be limited.

6. RECOMMENDED WORKFLOW:
   - Use MicroPython for: GPIO, basic I2C, prototyping
   - Use ModusToolbox for: Full sensor access, AI/ML, networking

7. DOCUMENTATION:
   - Board User Guide: Search "CY8CKIT-062S2-AI" on infineon.com
   - DEEPCRAFT Studio: www.imagimob.com
   - ModusToolbox: www.infineon.com/modustoolbox
"""

print(notes)

print("\n" + "=" * 60)
print("Example completed!")
print("=" * 60)

"""
Next Steps for CY8CKIT-062S2-AI Development:

MICROPYTHON PATH (This environment):
1. Use examples in this repository for GPIO, I2C, timers
2. Implement basic sensor reading via I2C
3. Log data to files or SD card
4. Build simple sensor monitoring applications

FULL AI/ML PATH (Recommended for this board):
1. Install ModusToolbox™ software
2. Install DEEPCRAFT™ Studio (formerly Imagimob Studio)
3. Use pre-built code examples from Infineon's GitHub
4. Collect sensor data using studio tools
5. Train ML models in DEEPCRAFT Studio
6. Deploy models to PSoC™ 6 MCU

HYBRID APPROACH:
- Use MicroPython for rapid prototyping
- Switch to ModusToolbox for production AI/ML deployment
- Leverage both ecosystems based on project phase

Resources:
- Board Page: https://www.infineon.com/cy8ckit-062s2-ai
- GitHub: https://github.com/Infineon/TARGET_CY8CKIT-062S2-AI
- MicroPython: https://github.com/infineon/micropython
- Community: https://community.infineon.com/
"""
