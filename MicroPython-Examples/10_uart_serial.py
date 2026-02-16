"""
UART Serial Communication Example for PSoC™ 6 MicroPython

This example demonstrates UART (Universal Asynchronous Receiver/Transmitter)
serial communication, commonly used for:
- Communicating with GPS modules
- Bluetooth modules (HC-05, HC-06)
- GSM/LTE modules
- Serial sensors and displays
- Debugging and logging
- Inter-device communication

UART Overview:
- Two-wire asynchronous protocol (TX - transmit, RX - receive)
- Common baud rates: 9600, 19200, 38400, 57600, 115200
- No clock signal needed
- Configurable data bits, parity, stop bits

Hardware Setup:
- Connect UART device's TX to PSoC™ 6 RX pin
- Connect UART device's RX to PSoC™ 6 TX pin
- Connect UART device's GND to PSoC™ 6 GND
- Optional: Flow control pins (RTS/CTS)

Note: UART voltage levels must match (3.3V for PSoC™ 6)
"""

from machine import UART, Pin
import time

# Configuration - Change these to match your board
UART_ID = 0         # UART peripheral number (0, 1, 2, etc.)
TX_PIN = 'P5_1'     # Transmit pin (example)
RX_PIN = 'P5_0'     # Receive pin (example)
BAUDRATE = 115200   # Communication speed (bits per second)

# UART Parameters
DATABITS = 8        # Data bits (7 or 8)
PARITY = None       # Parity: None, 0 (even), 1 (odd)
STOPBITS = 1        # Stop bits (1 or 2)
TIMEOUT = 1000      # Read timeout in milliseconds

print("UART Serial Communication Example")
print("=" * 50)
print(f"UART: {UART_ID}, Baudrate: {BAUDRATE}")
print(f"TX: {TX_PIN}, RX: {RX_PIN}")
print(f"Config: {DATABITS}{['N','E','O'][PARITY if PARITY else 0]}{STOPBITS}")
print("-" * 50)

# Initialize UART
try:
    uart = UART(UART_ID, 
                baudrate=BAUDRATE,
                bits=DATABITS,
                parity=PARITY,
                stop=STOPBITS,
                tx=Pin(TX_PIN),
                rx=Pin(RX_PIN),
                timeout=TIMEOUT)
    print("UART initialized successfully\n")
except Exception as e:
    print(f"Error initializing UART: {e}")
    raise

# Example 1: Sending data
print("Example 1: Sending data")
message = "Hello from PSoC6!\n"
bytes_sent = uart.write(message)
print(f"Sent {bytes_sent} bytes: '{message.strip()}'")

# Example 2: Sending binary data
print("\nExample 2: Sending binary data")
binary_data = bytes([0x01, 0x02, 0x03, 0x04, 0xFF])
uart.write(binary_data)
print(f"Sent binary: {[hex(b) for b in binary_data]}")

# Example 3: Reading data (blocking)
print("\nExample 3: Reading data (will wait for data)...")
print("Send some data to the UART...")

# Check if data is available
if uart.any():
    data = uart.read()  # Read all available data
    print(f"Received: {data}")
else:
    print("No data received (timeout)")

# Example 4: Reading specific number of bytes
print("\nExample 4: Reading specific number of bytes")
print("Waiting for 10 bytes...")
data = uart.read(10)  # Read exactly 10 bytes (or timeout)
if data:
    print(f"Received {len(data)} bytes: {data}")
else:
    print("Timeout - no data received")

# Example 5: Reading a line (until newline character)
print("\nExample 5: Reading a line")
print("Send a line ending with \\n...")
line = uart.readline()
if line:
    print(f"Received line: {line.decode('utf-8').strip()}")
else:
    print("Timeout - no line received")

# Example 6: Non-blocking read
print("\nExample 6: Non-blocking check and read")
for i in range(5):
    if uart.any():
        available = uart.any()
        print(f"  {available} bytes available")
        data = uart.read(available)
        print(f"  Read: {data}")
    else:
        print(f"  Check {i+1}: No data available")
    time.sleep(1)

# Example 7: Echo server
print("\nExample 7: Simple echo (5 seconds)")
print("Any data received will be echoed back")
start_time = time.time()

while time.time() - start_time < 5:
    if uart.any():
        data = uart.read()
        uart.write(data)  # Echo back
        print(f"Echoed: {data}")
    time.sleep_ms(100)

print("Echo stopped")

# Example 8: Parsing incoming data
print("\nExample 8: Command parser example")
print("Send commands: LED_ON, LED_OFF, STATUS")

def process_command(cmd):
    """Process received commands"""
    cmd = cmd.strip().upper()
    
    if cmd == "LED_ON":
        # led.on()  # Uncomment if LED is configured
        return "LED turned ON\n"
    elif cmd == "LED_OFF":
        # led.off()  # Uncomment if LED is configured
        return "LED turned OFF\n"
    elif cmd == "STATUS":
        return "System OK\n"
    else:
        return f"Unknown command: {cmd}\n"

# Run command parser for 10 seconds
start_time = time.time()
buffer = ""

while time.time() - start_time < 10:
    if uart.any():
        char = uart.read(1).decode('utf-8')
        buffer += char
        
        if char == '\n' or char == '\r':
            response = process_command(buffer)
            uart.write(response)
            print(f"Command: {buffer.strip()} -> {response.strip()}")
            buffer = ""
    
    time.sleep_ms(10)

print("Command parser stopped")

# Example 9: Sending formatted data
print("\nExample 9: Sending formatted sensor data")

# Simulate sensor readings
temperature = 25.5
humidity = 60.2
pressure = 1013.25

# JSON format
import json
sensor_data = {
    "temp": temperature,
    "humidity": humidity,
    "pressure": pressure,
    "timestamp": time.time()
}
json_str = json.dumps(sensor_data) + "\n"
uart.write(json_str)
print(f"Sent JSON: {json_str.strip()}")

# CSV format
csv_str = f"{temperature},{humidity},{pressure}\n"
uart.write(csv_str)
print(f"Sent CSV: {csv_str.strip()}")

# Custom format
custom_str = f"T:{temperature}C H:{humidity}% P:{pressure}hPa\n"
uart.write(custom_str)
print(f"Sent custom: {custom_str.strip()}")

print("\n" + "=" * 50)
print("UART example completed")

# Cleanup (optional)
# uart.deinit()

"""
UART Functions:
- uart.write(buf) - Write bytes/string
- uart.read([nbytes]) - Read bytes (all or specific number)
- uart.readline() - Read until newline
- uart.readinto(buf) - Read into existing buffer
- uart.any() - Check bytes available
- uart.flush() - Wait for all data to be sent

Common UART Applications:
1. GPS Modules (NMEA sentences)
   - Baudrate: Usually 9600
   - Read NMEA strings with readline()

2. Bluetooth Modules (HC-05, HC-06)
   - Baudrate: Usually 9600 or 38400
   - AT commands for configuration

3. GSM/LTE Modules
   - Baudrate: Varies (usually 115200)
   - AT commands for cellular communication

4. Serial Displays
   - Baudrate: Varies
   - Send display commands and data

5. Debugging
   - Print debug information
   - Log data to serial monitor

Error Handling Tips:
- Check uart.any() before reading to avoid blocking
- Use timeout to prevent infinite waiting
- Validate received data before processing
- Handle decode errors for non-ASCII data
- Add checksums for critical data

Baudrate Selection:
- 9600: Slow but reliable, good for long cables
- 19200: Common for older devices
- 38400: Good balance for many applications
- 57600: Faster, still reliable
- 115200: Common high-speed rate
- Higher rates possible but more error-prone
"""
