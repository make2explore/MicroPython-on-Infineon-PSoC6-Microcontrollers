"""
SPI Communication Example for PSoC™ 6 MicroPython

This example demonstrates SPI (Serial Peripheral Interface) communication,
commonly used for high-speed data transfer with sensors, displays, SD cards, etc.

SPI Overview:
- Four-wire serial protocol:
  * MOSI (Master Out Slave In) - Data from master to slave
  * MISO (Master In Slave Out) - Data from slave to master
  * SCK (Serial Clock) - Clock signal from master
  * CS/SS (Chip Select/Slave Select) - Device selection
- Full-duplex communication (simultaneous send/receive)
- Higher speed than I2C (up to several MHz)
- Single master, multiple slaves (each slave needs separate CS pin)

Hardware Setup:
- Connect SPI device's MOSI to PSoC™ 6 MOSI pin
- Connect SPI device's MISO to PSoC™ 6 MISO pin
- Connect SPI device's SCK to PSoC™ 6 SCK pin
- Connect SPI device's CS to a GPIO pin (you control this)
- Connect SPI device's GND to PSoC™ 6 GND
- Connect SPI device's VCC to 3.3V (or appropriate voltage)

Common SPI Pins on PSoC™ 6:
- Check your board's schematic for SPI pin assignments
- Multiple SPI peripherals may be available
"""

from machine import SPI, Pin
import time

# Configuration - Change these to match your board's SPI pins
SPI_ID = 0           # SPI bus number
MOSI_PIN = 'P12_0'   # Master Out Slave In (example pin)
MISO_PIN = 'P12_1'   # Master In Slave Out (example pin)
SCK_PIN = 'P12_2'    # Serial Clock (example pin)
CS_PIN = 'P12_3'     # Chip Select (you choose any available GPIO)

# SPI Configuration
SPI_BAUDRATE = 1000000  # 1 MHz (adjust based on device requirements)
SPI_POLARITY = 0        # Clock polarity (0 or 1)
SPI_PHASE = 0           # Clock phase (0 or 1)
SPI_BITS = 8            # Bits per transfer
SPI_FIRSTBIT = SPI.MSB  # MSB first (or SPI.LSB)

print("SPI Communication Example for PSoC™ 6")
print("=" * 50)
print(f"SPI Bus: {SPI_ID}")
print(f"MOSI: {MOSI_PIN}, MISO: {MISO_PIN}, SCK: {SCK_PIN}")
print(f"CS: {CS_PIN}")
print(f"Baudrate: {SPI_BAUDRATE} Hz")
print("-" * 50)

# Initialize Chip Select pin (active low)
cs = Pin(CS_PIN, Pin.OUT)
cs.value(1)  # Deselect (CS high)

# Initialize SPI
try:
    spi = SPI(SPI_ID,
              baudrate=SPI_BAUDRATE,
              polarity=SPI_POLARITY,
              phase=SPI_PHASE,
              bits=SPI_BITS,
              firstbit=SPI_FIRSTBIT,
              sck=Pin(SCK_PIN),
              mosi=Pin(MOSI_PIN),
              miso=Pin(MISO_PIN))
    print("SPI initialized successfully\n")
except Exception as e:
    print(f"Error initializing SPI: {e}")
    raise

# Helper function to select/deselect device
def select():
    """Assert chip select (active low)"""
    cs.value(0)
    time.sleep_us(1)  # Small delay for CS setup time

def deselect():
    """Deassert chip select"""
    time.sleep_us(1)  # Small delay for CS hold time
    cs.value(1)

# Example 1: Write data to SPI device
print("Example 1: Writing data...")
select()
data_to_write = bytes([0x01, 0x02, 0x03, 0x04])
spi.write(data_to_write)
deselect()
print(f"Wrote: {[hex(b) for b in data_to_write]}")

# Example 2: Read data from SPI device
print("\nExample 2: Reading data...")
select()
read_buffer = bytearray(4)  # Buffer to store received data
spi.readinto(read_buffer)
deselect()
print(f"Read: {[hex(b) for b in read_buffer]}")

# Example 3: Write and read simultaneously (full-duplex)
print("\nExample 3: Write and read simultaneously...")
select()
write_data = bytes([0xAA, 0xBB, 0xCC, 0xDD])
read_data = bytearray(len(write_data))
spi.write_readinto(write_data, read_data)
deselect()
print(f"Wrote: {[hex(b) for b in write_data]}")
print(f"Read:  {[hex(b) for b in read_data]}")

# Example 4: Reading a register from an SPI device
print("\nExample 4: Reading a register...")
REGISTER_ADDR = 0x00  # Example register address
READ_FLAG = 0x80      # Some devices use MSB=1 for read operations

select()
# Send register address with read flag
spi.write(bytes([REGISTER_ADDR | READ_FLAG]))
# Read the register value
register_value = bytearray(1)
spi.readinto(register_value)
deselect()
print(f"Register 0x{REGISTER_ADDR:02X} = 0x{register_value[0]:02X}")

# Example 5: Writing to a register
print("\nExample 5: Writing to a register...")
WRITE_REGISTER = 0x01
WRITE_VALUE = 0x42

select()
# Send register address (no read flag)
# Then send the value to write
spi.write(bytes([WRITE_REGISTER, WRITE_VALUE]))
deselect()
print(f"Wrote 0x{WRITE_VALUE:02X} to register 0x{WRITE_REGISTER:02X}")

# Example 6: Multi-byte transfer
print("\nExample 6: Multi-byte data transfer...")
select()
# Write command or address
spi.write(bytes([0x03, 0x00, 0x00]))  # Example: Read from address 0x0000
# Read multiple bytes
data = bytearray(8)
spi.readinto(data)
deselect()
print(f"Read {len(data)} bytes: {[hex(b) for b in data]}")

# Cleanup
print("\n" + "=" * 50)
print("SPI example completed")
print("\nNote: Actual behavior depends on your connected SPI device.")
print("Refer to your device's datasheet for command sequences.")

# Deinitialize SPI (optional)
# spi.deinit()

"""
Common SPI Devices and Applications:
- SD Cards - Data storage
- Flash Memory (W25Q, AT25, etc.) - Non-volatile storage
- OLED/LCD Displays - Graphics and text
- Accelerometers/Gyroscopes - Motion sensing
- ADCs/DACs - High-speed analog conversion
- Radio modules (nRF24L01, etc.) - Wireless communication

SPI Mode Configuration (CPOL/CPHA):
- Mode 0: CPOL=0, CPHA=0 (most common)
- Mode 1: CPOL=0, CPHA=1
- Mode 2: CPOL=1, CPHA=0
- Mode 3: CPOL=1, CPHA=1

SPI Functions:
- spi.write(buf) - Write bytes
- spi.read(nbytes) - Read bytes (sends dummy data)
- spi.readinto(buf) - Read into existing buffer
- spi.write_readinto(write_buf, read_buf) - Full-duplex transfer

Tips:
1. Check device datasheet for correct SPI mode and speed
2. Some devices need delays between CS assertion and data transfer
3. Remember to control CS pin manually in MicroPython
4. Use logic analyzer to debug SPI communication issues
"""
