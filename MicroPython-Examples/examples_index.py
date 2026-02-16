"""
MicroPython Examples for PSoC™ 6 - Index and Catalog

This file provides an overview of all available examples and how to use them.
Each example is self-contained and includes detailed comments.

Repository Structure:
examples/
├── 01_led_blink.py           - Basic GPIO: LED blinking
├── 02_led_on_signal.py        - Using Signal class for active-low LEDs
├── 03_button_input.py         - Reading digital input from buttons
├── 04_adc_analog_input.py     - Analog-to-Digital conversion
├── 05_pwm_led_fade.py         - PWM for LED brightness control
├── 06_i2c_communication.py    - I2C bus communication
├── 07_file_operations.py      - Filesystem read/write operations
├── 08_repl_examples.py        - Interactive REPL commands reference
├── 09_spi_communication.py    - SPI bus communication
├── 10_uart_serial.py          - UART/Serial communication
├── 11_timer_interrupt.py      - Timers and interrupt handling
├── board_config.py            - Board-specific pin configurations
└── examples_index.py          - This file
"""

# ============================================================================
# QUICK START GUIDE
# ============================================================================

QUICK_START = """
Quick Start Guide - Running Examples
=====================================

1. SETUP YOUR BOARD
   - Install MicroPython on your PSoC™ 6 board
   - Connect via Arduino Lab for MicroPython or Thonny IDE
   - Verify connection by typing in REPL: >>> print('Hello PSoC6!')

2. UPLOAD EXAMPLES
   - Use your IDE's file upload feature
   - Upload examples to your board's filesystem
   - Alternatively, copy-paste code into the REPL

3. RUN AN EXAMPLE
   Method 1 (REPL): 
     >>> import 01_led_blink
   
   Method 2 (IDE): 
     - Open the example file
     - Click "Run" in your IDE
   
   Method 3 (Auto-run on boot):
     - Rename example to 'main.py'
     - Save to board's filesystem
     - Press board's reset button

4. MODIFY FOR YOUR BOARD
   - Check LED_PIN and other pin configurations
   - Update to match your specific board
   - See board_config.py for pre-configured pin mappings
"""

# ============================================================================
# EXAMPLES CATALOG
# ============================================================================

EXAMPLES = {
    'beginner': {
        'description': 'Start here if you are new to MicroPython or embedded programming',
        'examples': [
            {
                'file': '01_led_blink.py',
                'title': 'LED Blink',
                'description': 'Basic GPIO control - blinks the onboard LED',
                'concepts': ['GPIO output', 'Pin control', 'Delays', 'While loops'],
                'hardware': ['Onboard LED'],
                'difficulty': '⭐ Beginner'
            },
            {
                'file': '02_led_on_signal.py',
                'title': 'LED Control with Signal',
                'description': 'Using Signal class for active-low LEDs',
                'concepts': ['Signal class', 'Active-low logic', 'Pin inversion'],
                'hardware': ['Onboard LED'],
                'difficulty': '⭐ Beginner'
            },
            {
                'file': '03_button_input.py',
                'title': 'Button Input',
                'description': 'Reading digital input from a button',
                'concepts': ['GPIO input', 'Pull-up resistors', 'Debouncing'],
                'hardware': ['Button', 'LED'],
                'difficulty': '⭐ Beginner'
            },
            {
                'file': '08_repl_examples.py',
                'title': 'REPL Examples',
                'description': 'Interactive commands reference for the REPL',
                'concepts': ['REPL usage', 'Interactive programming', 'Quick testing'],
                'hardware': ['None required'],
                'difficulty': '⭐ Beginner'
            }
        ]
    },
    
    'intermediate': {
        'description': 'Peripheral interfacing and data handling',
        'examples': [
            {
                'file': '04_adc_analog_input.py',
                'title': 'Analog Input (ADC)',
                'description': 'Reading analog sensors using ADC',
                'concepts': ['ADC', 'Analog-to-digital conversion', 'Voltage reading'],
                'hardware': ['Potentiometer or analog sensor'],
                'difficulty': '⭐⭐ Intermediate'
            },
            {
                'file': '05_pwm_led_fade.py',
                'title': 'PWM LED Fade',
                'description': 'Smooth LED brightness control using PWM',
                'concepts': ['PWM', 'Duty cycle', 'Frequency control'],
                'hardware': ['LED'],
                'difficulty': '⭐⭐ Intermediate'
            },
            {
                'file': '07_file_operations.py',
                'title': 'File Operations',
                'description': 'Reading, writing, and managing files',
                'concepts': ['Filesystem', 'Data logging', 'CSV format'],
                'hardware': ['None required'],
                'difficulty': '⭐⭐ Intermediate'
            },
            {
                'file': '11_timer_interrupt.py',
                'title': 'Timers and Interrupts',
                'description': 'Non-blocking timing and event handling',
                'concepts': ['Timers', 'Interrupts', 'Callbacks', 'Event-driven programming'],
                'hardware': ['LED', 'Button (optional)'],
                'difficulty': '⭐⭐⭐ Intermediate-Advanced'
            }
        ]
    },
    
    'advanced': {
        'description': 'Communication protocols and complex interfacing',
        'examples': [
            {
                'file': '06_i2c_communication.py',
                'title': 'I2C Communication',
                'description': 'Interfacing with I2C sensors and peripherals',
                'concepts': ['I2C protocol', 'Bus scanning', 'Multi-device communication'],
                'hardware': ['I2C sensor (e.g., temperature sensor, accelerometer)'],
                'difficulty': '⭐⭐⭐ Advanced'
            },
            {
                'file': '09_spi_communication.py',
                'title': 'SPI Communication',
                'description': 'High-speed data transfer using SPI',
                'concepts': ['SPI protocol', 'Full-duplex communication', 'Chip select'],
                'hardware': ['SPI device (e.g., SD card, display, sensor)'],
                'difficulty': '⭐⭐⭐ Advanced'
            },
            {
                'file': '10_uart_serial.py',
                'title': 'UART Serial Communication',
                'description': 'Serial communication with external devices',
                'concepts': ['UART', 'Serial protocol', 'Command parsing', 'Data formats'],
                'hardware': ['UART device (e.g., GPS, Bluetooth module)'],
                'difficulty': '⭐⭐⭐ Advanced'
            }
        ]
    },
    
    'utilities': {
        'description': 'Helper modules and configurations',
        'examples': [
            {
                'file': 'board_config.py',
                'title': 'Board Configuration',
                'description': 'Pin definitions for all supported boards',
                'concepts': ['Board abstraction', 'Code portability', 'Pin mapping'],
                'hardware': ['Any PSoC™ 6 board'],
                'difficulty': '⭐ Beginner'
            }
        ]
    }
}

# ============================================================================
# LEARNING PATHS
# ============================================================================

LEARNING_PATHS = {
    'absolute_beginner': [
        '08_repl_examples.py',      # Get familiar with REPL
        '01_led_blink.py',          # First program
        '02_led_on_signal.py',      # Understanding Signal class
        '03_button_input.py',       # Reading inputs
        '04_adc_analog_input.py',   # Analog sensors
    ],
    
    'embedded_developer': [
        '01_led_blink.py',          # GPIO basics
        '05_pwm_led_fade.py',       # PWM control
        '11_timer_interrupt.py',    # Timers and interrupts
        '06_i2c_communication.py',  # I2C protocol
        '09_spi_communication.py',  # SPI protocol
        '10_uart_serial.py',        # UART communication
    ],
    
    'iot_developer': [
        '04_adc_analog_input.py',   # Sensor reading
        '07_file_operations.py',    # Data logging
        '06_i2c_communication.py',  # Sensor interfacing
        '10_uart_serial.py',        # Communication modules
        '11_timer_interrupt.py',    # Periodic tasks
    ]
}

# ============================================================================
# HARDWARE REQUIREMENTS BY EXAMPLE
# ============================================================================

HARDWARE_REQUIREMENTS = """
Hardware Requirements by Example
==================================

REQUIRED FOR ALL EXAMPLES:
- PSoC™ 6 development board
- USB cable
- Computer with MicroPython IDE

ADDITIONAL HARDWARE:

Minimal Setup (Board Only):
  01_led_blink.py
  02_led_on_signal.py
  07_file_operations.py
  08_repl_examples.py
  board_config.py

With Button:
  03_button_input.py
  11_timer_interrupt.py (optional)

With Potentiometer/Sensor:
  04_adc_analog_input.py
  - Connect to ADC pin (e.g., P10_0)
  - Connect to GND and 3.3V

With I2C Device:
  06_i2c_communication.py
  - Temperature sensor (e.g., LM75, TMP102)
  - Accelerometer (e.g., ADXL345, MPU6050)
  - OLED Display (e.g., SSD1306)
  - Any I2C sensor or peripheral

With SPI Device:
  09_spi_communication.py
  - SD Card module
  - SPI display (e.g., ILI9341)
  - SPI sensor or peripheral

With UART Device:
  10_uart_serial.py
  - GPS module
  - Bluetooth module (HC-05, HC-06)
  - GSM module
  - Another microcontroller
"""

# ============================================================================
# COMMON ISSUES AND SOLUTIONS
# ============================================================================

TROUBLESHOOTING = """
Common Issues and Solutions
============================

ISSUE: "ImportError: no module named 'X'"
SOLUTION: 
  - Module not available in MicroPython
  - Check MicroPython library documentation
  - Some Python stdlib modules are not included

ISSUE: "OSError: [Errno 19] ENODEV"
SOLUTION:
  - Hardware not connected or wrong pin
  - Check pin configuration in code
  - Verify hardware connections

ISSUE: LED not working
SOLUTION:
  - Check LED_PIN matches your board
  - Use board_config.py for correct pins
  - Some LEDs are active-low (use Signal class)

ISSUE: I2C/SPI device not found
SOLUTION:
  - Verify wiring (SDA, SCL, MOSI, MISO, etc.)
  - Check pull-up resistors (required for I2C)
  - Verify power supply to device (3.3V)
  - Scan bus to confirm address

ISSUE: Button not responding
SOLUTION:
  - Check BUTTON_PIN configuration
  - Enable pull-up resistor
  - Add debouncing delay
  - Verify button connections

ISSUE: Code runs in REPL but not as main.py
SOLUTION:
  - Check for syntax errors
  - Ensure main.py is in root directory
  - Check file was saved to board (not computer)
  - Look for exception messages on boot

ISSUE: Out of memory
SOLUTION:
  - Call gc.collect() to free memory
  - Reduce buffer sizes
  - Delete unused variables
  - Simplify data structures
"""

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def print_catalog():
    """Print all examples organized by category"""
    print("=" * 70)
    print("PSoC™ 6 MicroPython Examples Catalog")
    print("=" * 70)
    
    for category, info in EXAMPLES.items():
        print(f"\n{category.upper()}")
        print(f"{info['description']}")
        print("-" * 70)
        
        for ex in info['examples']:
            print(f"\n📁 {ex['file']}")
            print(f"   {ex['title']} - {ex['difficulty']}")
            print(f"   {ex['description']}")
            print(f"   Concepts: {', '.join(ex['concepts'])}")
            print(f"   Hardware: {', '.join(ex['hardware'])}")

def print_learning_path(path_name):
    """Print examples for a specific learning path"""
    if path_name not in LEARNING_PATHS:
        print(f"Unknown learning path: {path_name}")
        print(f"Available paths: {', '.join(LEARNING_PATHS.keys())}")
        return
    
    print(f"\n{'='*70}")
    print(f"Learning Path: {path_name.replace('_', ' ').title()}")
    print(f"{'='*70}")
    
    for i, example in enumerate(LEARNING_PATHS[path_name], 1):
        print(f"{i}. {example}")
    
    print(f"\nFollow these examples in order for the best learning experience!")

def get_example_info(filename):
    """Get information about a specific example"""
    for category, info in EXAMPLES.items():
        for ex in info['examples']:
            if ex['file'] == filename:
                return ex
    return None

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print(__doc__)
    print(QUICK_START)
    print("\n")
    print_catalog()
    print("\n")
    print(HARDWARE_REQUIREMENTS)
    print("\n")
    print(TROUBLESHOOTING)
    
    print("\n" + "="*70)
    print("LEARNING PATHS")
    print("="*70)
    for path_name in LEARNING_PATHS:
        print(f"  - {path_name}")
    
    print("\nTo see a specific learning path, use:")
    print("  print_learning_path('absolute_beginner')")

"""
Additional Resources:
=====================

Official Documentation:
- PSoC™ 6 Quick Reference: 
  https://ifx-micropython.readthedocs.io/en/latest/psoc6/quickref.html
  
- MicroPython Documentation:
  https://docs.micropython.org/
  
- Infineon GitHub:
  https://github.com/infineon/micropython

Community:
- MicroPython Forum: https://forum.micropython.org/
- Infineon Community: https://community.infineon.com/

Getting Help:
1. Check this examples_index.py for overview
2. Read the example file's comments
3. Check troubleshooting section
4. Search the forums
5. Open an issue on GitHub
"""
