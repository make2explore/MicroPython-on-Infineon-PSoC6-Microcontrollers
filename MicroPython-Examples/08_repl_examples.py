"""
REPL (Read-Eval-Print Loop) Interactive Examples
PSoC™ 6 MicroPython

This file contains examples to try in the MicroPython REPL.
The REPL is an interactive Python prompt where you can type commands
and see immediate results.

To access the REPL:
1. Connect to your PSoC™ 6 board using your IDE or serial terminal
2. You'll see the >>> prompt
3. Type these commands and press Enter

=====================================================================
BASIC PYTHON COMMANDS
=====================================================================

# Print hello world
>>> print('Hello from PSoC6!')
Hello from PSoC6!

# Basic math
>>> 2 + 2
4

>>> 10 * 5
50

>>> 2 ** 8  # 2 to the power of 8
256

# Variables
>>> x = 42
>>> y = 8
>>> x + y
50

# Strings
>>> name = "PSoC6"
>>> print(f"Hello {name}!")
Hello PSoC6!

# Lists
>>> sensors = ['temp', 'humidity', 'pressure']
>>> sensors[0]
'temp'

>>> len(sensors)
3

=====================================================================
SYSTEM INFORMATION
=====================================================================

# Check MicroPython version
>>> import sys
>>> sys.version
'3.4.0'

# Check platform
>>> sys.platform
'psoc6'

# Check available memory
>>> import gc
>>> gc.mem_free()
104560  # Example output (bytes)

# Collect garbage (free up memory)
>>> gc.collect()

=====================================================================
GPIO - LED CONTROL
=====================================================================

# Import required modules
>>> from machine import Pin

# Turn on LED (change pin for your board)
>>> led = Pin('P13_7', Pin.OUT)
>>> led.on()

# Turn off LED
>>> led.off()

# Toggle LED
>>> led.toggle()

# Read LED state
>>> led.value()
0  # or 1

# Using Signal for active-low LEDs
>>> from machine import Signal
>>> led = Signal(Pin('P13_7'), invert=True)
>>> led.on()   # Actually sets pin LOW
>>> led.off()  # Actually sets pin HIGH

=====================================================================
ANALOG INPUT (ADC)
=====================================================================

# Read analog voltage
>>> from machine import ADC, Pin
>>> adc = ADC(Pin('P10_0'))
>>> adc.read_u16()
32768  # Raw value (0-65535)

# Convert to voltage
>>> raw = adc.read_u16()
>>> voltage = (raw / 65535) * 3.3
>>> print(f'{voltage:.2f}V')
1.65V

=====================================================================
PWM OUTPUT
=====================================================================

# Create PWM on LED pin
>>> from machine import PWM, Pin
>>> pwm = PWM(Pin('P13_7'))
>>> pwm.freq(1000)  # Set 1kHz frequency

# Set 50% duty cycle
>>> pwm.duty_u16(32768)

# Set 75% duty cycle
>>> pwm.duty_u16(49152)

# Turn off PWM
>>> pwm.deinit()

=====================================================================
TIMING AND DELAYS
=====================================================================

# Import time module
>>> import time

# Get current time (seconds since boot)
>>> time.time()
123.456

# Sleep for 1 second
>>> time.sleep(1)

# Sleep for 500 milliseconds
>>> time.sleep_ms(500)

# Sleep for 100 microseconds
>>> time.sleep_us(100)

# Measure execution time
>>> start = time.ticks_ms()
>>> time.sleep(1)
>>> elapsed = time.ticks_diff(time.ticks_ms(), start)
>>> print(f'{elapsed}ms')
1000ms

=====================================================================
I2C COMMUNICATION
=====================================================================

# Initialize I2C
>>> from machine import I2C, Pin
>>> i2c = I2C(0, scl=Pin('P6_0'), sda=Pin('P6_1'))

# Scan for devices
>>> devices = i2c.scan()
>>> print([hex(d) for d in devices])
['0x48', '0x68']  # Example output

# Read from device
>>> data = i2c.readfrom(0x48, 2)
>>> print(data)
b'\x12\x34'

=====================================================================
FILE OPERATIONS
=====================================================================

# Write to a file
>>> with open('test.txt', 'w') as f:
...     f.write('Hello PSoC6!')

# Read from a file
>>> with open('test.txt', 'r') as f:
...     print(f.read())
Hello PSoC6!

# List files
>>> import os
>>> os.listdir()
['boot.py', 'main.py', 'test.txt']

# Get file info
>>> os.stat('test.txt')
(32768, 0, 0, 0, 0, 0, 12, 0, 0, 0)

# Delete a file
>>> os.remove('test.txt')

=====================================================================
INTERRUPTS (BUTTON PRESS)
=====================================================================

# Define interrupt handler
>>> def button_handler(pin):
...     print('Button pressed!')

# Set up interrupt on button pin
>>> from machine import Pin
>>> button = Pin('P0_4', Pin.IN, Pin.PULL_UP)
>>> button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

# Now press the button to see the message

# Disable interrupt
>>> button.irq(handler=None)

=====================================================================
USEFUL COMMANDS
=====================================================================

# Get help on a module
>>> help(machine)

# Get help on a specific object
>>> help(Pin)

# List available attributes
>>> dir(machine)

# Clear screen (may not work in all terminals)
>>> print('\033[2J\033[H')

# Soft reset the board
>>> import machine
>>> machine.soft_reset()

# Hard reset the board (reboots)
>>> machine.reset()

=====================================================================
DEBUGGING TIPS
=====================================================================

# Print variable type
>>> x = 42
>>> type(x)
<class 'int'>

# Check if variable exists
>>> 'led' in dir()
True

# Memory usage
>>> import gc
>>> gc.mem_free()
>>> gc.mem_alloc()

# Exception handling
>>> try:
...     result = 10 / 0
... except ZeroDivisionError:
...     print('Cannot divide by zero!')
Cannot divide by zero!

=====================================================================
EXITING REPL
=====================================================================

# To exit a running program, press: Ctrl+C
# To soft reset the board, press: Ctrl+D
# To paste multi-line code, use: Ctrl+E (paste mode)

=====================================================================

For more information:
- PSoC™ 6 MicroPython Quick Reference: 
  https://ifx-micropython.readthedocs.io/en/latest/psoc6/quickref.html
- MicroPython Documentation:
  https://docs.micropython.org/

"""

# This file is for reference only - copy and paste commands into the REPL
print(__doc__)
