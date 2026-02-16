"""
File Operations Example for PSoC™ 6 MicroPython

This example demonstrates working with the filesystem on PSoC™ 6.
MicroPython includes a small filesystem for storing scripts and data.

Filesystem Features:
- Persistent storage (survives power cycles)
- Standard Python file operations
- Useful for data logging, configuration, etc.

Common Files:
- main.py - Automatically runs on boot
- boot.py - Runs before main.py (for system configuration)

Note: Filesystem is small (~64KB), so manage space carefully
"""

import time
import os

print("File Operations Example for PSoC™ 6")
print("=" * 50)

# Example 1: Writing to a file
print("\n1. Writing to a file...")
filename = 'data.txt'

with open(filename, 'w') as f:
    f.write('PSoC™ 6 MicroPython File Example\n')
    f.write('Temperature: 25.5°C\n')
    f.write('Humidity: 60%\n')
    f.write('Timestamp: {}\n'.format(time.time()))

print(f"   Data written to '{filename}'")

# Example 2: Reading from a file
print("\n2. Reading from a file...")
with open(filename, 'r') as f:
    content = f.read()
    print("   File contents:")
    print("   " + "-" * 45)
    for line in content.split('\n'):
        if line:  # Skip empty lines
            print(f"   {line}")
    print("   " + "-" * 45)

# Example 3: Appending to a file
print("\n3. Appending to a file...")
with open(filename, 'a') as f:
    f.write(f'Appended data at: {time.time()}\n')
    f.write('Status: OK\n')

print(f"   Additional data appended to '{filename}'")

# Example 4: Reading line by line
print("\n4. Reading file line by line...")
with open(filename, 'r') as f:
    line_num = 1
    for line in f:
        print(f"   Line {line_num}: {line.strip()}")
        line_num += 1

# Example 5: Creating a data log
print("\n5. Creating a sensor data log...")
log_file = 'sensor_log.csv'

# Write CSV header
with open(log_file, 'w') as f:
    f.write('Timestamp,Temperature,Humidity\n')

# Simulate logging sensor data
print(f"   Logging data to '{log_file}'...")
for i in range(5):
    timestamp = time.time()
    temperature = 25.0 + i * 0.5  # Simulated temperature
    humidity = 60 + i * 2         # Simulated humidity
    
    with open(log_file, 'a') as f:
        f.write(f'{timestamp},{temperature},{humidity}\n')
    
    print(f"   Logged: T={temperature}°C, H={humidity}%")
    time.sleep(0.5)

# Example 6: Listing files
print("\n6. Listing files in the filesystem...")
try:
    files = os.listdir()
    print(f"   Found {len(files)} file(s):")
    for file in files:
        try:
            stat = os.stat(file)
            size = stat[6]  # File size in bytes
            print(f"   - {file:20s} ({size} bytes)")
        except:
            print(f"   - {file}")
except Exception as e:
    print(f"   Error listing files: {e}")

# Example 7: Checking if file exists
print("\n7. Checking file existence...")
test_files = ['data.txt', 'sensor_log.csv', 'nonexistent.txt']

for fname in test_files:
    try:
        os.stat(fname)
        print(f"   '{fname}' exists")
    except OSError:
        print(f"   '{fname}' does not exist")

# Example 8: Deleting a file
print("\n8. File management...")
print("   To delete a file, use: os.remove('filename.txt')")
print("   To rename a file, use: os.rename('old.txt', 'new.txt')")

# Cleanup example (commented out for safety)
# os.remove('sensor_log.csv')
# print("   Deleted 'sensor_log.csv'")

print("\n" + "=" * 50)
print("File operations example completed!")
print("\nTip: Create 'main.py' to have code run automatically on boot")

"""
Auto-run Example:
To make a script run automatically when the board powers up,
save it as 'main.py' in the filesystem.

Example main.py:
-----------------
from machine import Pin
import time

led = Pin('P13_7', Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
-----------------

Filesystem Functions:
- open(file, mode) - Open file ('r', 'w', 'a', 'rb', 'wb', 'ab')
- os.listdir() - List files in current directory
- os.stat(file) - Get file information
- os.remove(file) - Delete a file
- os.rename(old, new) - Rename a file
- os.mkdir(dir) - Create a directory
- os.chdir(dir) - Change directory
"""
