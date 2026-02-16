# MicroPython on Infineon PSoC™ 6 Microcontrollers

Welcome to the comprehensive guide for running MicroPython on Infineon PSoC™ 6 microcontrollers. This repository provides everything you need to get started with embedded Python development on PSoC™ 6 devices.

## 📋 Table of Contents

- [Overview](#overview)
- [Supported Boards](#supported-boards)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Development Environments](#development-environments)
- [Examples](#examples)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Resources](#resources)

## 🌟 Overview

MicroPython is a lean and efficient implementation of Python 3 designed specifically for microcontrollers and embedded systems. This port brings the power and simplicity of Python to Infineon's PSoC™ 6 family of ultra-low-power, high-performance microcontrollers.

### Why MicroPython on PSoC™ 6?

- **Rapid Prototyping**: Write and test code interactively using the REPL
- **Python Simplicity**: Leverage familiar Python syntax for embedded development
- **Powerful Hardware**: Access PSoC™ 6's dual ARM Cortex cores, BLE, Wi-Fi, and configurable peripherals
- **Rich Ecosystem**: Utilize MicroPython's extensive library support
- **Educational**: Perfect for learning embedded systems programming

## 🔧 Supported Boards

This MicroPython port supports the following PSoC™ 6 development boards:

| Board Model | Features | LED Pin |
|------------|----------|---------|
| **CY8CPROTO-062-4343W** | Wi-Fi & Bluetooth, Prototyping Kit | P13_7 |
| **CY8CPROTO-063-BLE** | Bluetooth Low Energy, Prototyping Kit | P6_3 |
| **CY8CKIT-062-BLE** | PSoC™ 6 BLE Pioneer Kit | P13_7 |
| **CY8CKIT-062-WIFI-BT** | PSoC™ 6 Wi-Fi BT Pioneer Kit | P13_7 |
| **CY8CKIT-062S2-43012** | PSoC™ 62S2 Wi-Fi BT Pioneer Kit | P13_7 |

All boards feature:
- Dual-core ARM Cortex-M4 (150 MHz) and Cortex-M0+ (100 MHz)
- On-board KitProg debugger/programmer
- Rich peripheral set (GPIO, ADC, PWM, I2C, SPI, UART, etc.)
- Ultra-low power modes

## 📦 Prerequisites

### Hardware Requirements
- One of the supported PSoC™ 6 development boards
- USB cable (typically USB Type-A to Micro-B)
- Computer running Windows, macOS, or Linux

### Software Requirements
- **Python 3.8 or later** - [Download here](https://www.python.org/downloads/)
- **pip** package manager (included with Python 3.4+)
- Terminal or command prompt application

## 🚀 Quick Start

Get up and running in just a few commands:

```bash
# Create a working directory
mkdir mpy-psoc6
cd mpy-psoc6

# Download the installation utility
curl -s -L https://raw.githubusercontent.com/infineon/micropython/ports-psoc6-main/tools/psoc6/mpy-psoc6.py > mpy-psoc6.py

# Install dependencies
pip install requests

# Connect your PSoC™ 6 board and run the setup
python mpy-psoc6.py device-setup
```

That's it! Your PSoC™ 6 board is now running MicroPython.

## 💻 Installation

### Detailed Installation Steps

1. **Create a Project Folder**
   ```bash
   mkdir mpy-psoc6
   cd mpy-psoc6
   ```

2. **Download the mpy-psoc6 Utility**
   ```bash
   curl -s -L https://raw.githubusercontent.com/infineon/micropython/ports-psoc6-main/tools/psoc6/mpy-psoc6.py > mpy-psoc6.py
   ```

3. **Install Python Dependencies**
   ```bash
   pip install requests
   ```

4. **Connect Your Board**
   - Use the **KitProg USB port** (not the Target USB port)
   - Ensure the power LED illuminates

5. **Run Device Setup**
   ```bash
   python mpy-psoc6.py device-setup
   ```
   
   The script will:
   - Detect your connected board
   - Download the appropriate firmware
   - Flash MicroPython to your device
   - Verify the installation

## 🛠️ Development Environments

Choose from several excellent development environments:

### Arduino Lab for MicroPython (Recommended for Beginners)
- User-friendly GUI with REPL console
- File management and upload capabilities
- No installation required (portable)

**Download**: [labs.arduino.cc/en/labs/micropython](https://labs.arduino.cc/en/labs/micropython)

### Thonny IDE
- Beginner-friendly Python IDE
- Built-in MicroPython support
- Filesystem browser for easy file management

**Download**: [thonny.org](https://thonny.org/)

**Setup**:
1. Install Thonny
2. Click the interpreter selector (bottom-right)
3. Select "MicroPython (generic)"
4. Choose your board's COM port

### Command-Line Tools
For advanced users:
- **screen** (Linux/macOS)
- **PuTTY** (Windows)
- **picocom** or **minicom** (Linux)

Example with screen:
```bash
screen /dev/ttyACM0 115200
```

## 📚 Examples

### Hello World - LED Blink

```python
from machine import Pin
import time

# Use your board's LED pin (see table above)
led = Pin('P13_7', Pin.OUT)
led.off()

while True:
    time.sleep_ms(1000)
    led.toggle()
```

### Button Input

```python
from machine import Pin
import time

# Configure pins (check your board's schematic)
button = Pin('P0_4', Pin.IN, Pin.PULL_UP)
led = Pin('P13_7', Pin.OUT)
led.off()

while True:
    if button.value() == 0:  # Button pressed (active-low)
        led.on()
    else:
        led.off()
    time.sleep_ms(50)  # Debounce delay
```

### Analog Input (ADC)

```python
from machine import ADC, Pin
import time

adc = ADC(Pin('P10_0'))

while True:
    raw_value = adc.read_u16()
    voltage = (raw_value / 65535) * 3.3
    print(f'Voltage: {voltage:.2f}V')
    time.sleep(1)
```

### PWM - LED Fade

```python
from machine import Pin, PWM
import time

pwm_led = PWM(Pin('P13_7'))
pwm_led.freq(1000)

while True:
    # Fade in
    for duty in range(0, 65536, 256):
        pwm_led.duty_u16(duty)
        time.sleep_ms(10)
    
    # Fade out
    for duty in range(65535, 0, -256):
        pwm_led.duty_u16(duty)
        time.sleep_ms(10)
```

### I2C Communication

```python
from machine import I2C, Pin

# Initialize I2C (check your board's I2C pins)
i2c = I2C(0, scl=Pin('P6_0'), sda=Pin('P6_1'), freq=400000)

# Scan for devices
devices = i2c.scan()
print('I2C devices found:', [hex(device) for device in devices])

# Read from a device
if 0x48 in devices:
    data = i2c.readfrom(0x48, 2)
    print('Data:', data)
```

## 📖 Documentation

### Official Resources
- **PSoC™ 6 MicroPython Quick Reference**: [ifx-micropython.readthedocs.io](https://ifx-micropython.readthedocs.io/en/latest/psoc6/quickref.html)
- **Full Documentation**: [docs.micropython.org](https://docs.micropython.org/)
- **Infineon GitHub Repository**: [github.com/infineon/micropython](https://github.com/infineon/micropython)

### API Documentation
- `machine` module - Hardware access (GPIO, ADC, PWM, I2C, SPI, etc.)
- `time` module - Time and delays
- `os` module - Filesystem operations
- `sys` module - System-specific parameters

### Advanced Topics
- Bluetooth Low Energy (BLE) communication
- Wi-Fi connectivity (boards with Wi-Fi support)
- Dual-core programming (Cortex-M4 and Cortex-M0+)
- Low-power modes and sleep states
- Real-time clock (RTC) and timers
- DMA and interrupts

## 🔍 Troubleshooting

### Board Not Detected

**Symptoms**: Device setup script can't find the board

**Solutions**:
- Verify USB cable is connected to the **KitProg port** (not Target USB)
- Try a different USB cable (some are power-only)
- Check Device Manager (Windows) or `lsusb` (Linux) to confirm board detection
- Install USB drivers if necessary (usually automatic)

### Installation Failed

**Symptoms**: Device setup script errors or fails

**Solutions**:
- Verify Python version: `python --version` (must be 3.8+)
- Ensure pip is installed: `pip --version`
- Check `requests` package: `pip install requests`
- Run with administrator/sudo privileges if permission errors occur

### REPL Not Responding

**Symptoms**: No response to commands in the REPL

**Solutions**:
- Press `Ctrl+C` to interrupt any running program
- Press `Ctrl+D` to soft-reset the board
- Disconnect and reconnect USB cable
- Verify correct COM port is selected in your IDE

### Code Not Auto-Running

**Symptoms**: `main.py` doesn't run on power-up

**Solutions**:
- Ensure filename is exactly `main.py` (case-sensitive)
- Verify file is saved to the board's filesystem (not your computer)
- Check for syntax errors by running code manually first
- Press reset button on board after saving

### Import Errors

**Symptoms**: `ImportError: no module named 'X'`

**Solutions**:
- Verify you're using MicroPython-compatible libraries
- Some standard Python modules aren't available in MicroPython
- Check the [MicroPython library index](https://docs.micropython.org/en/latest/library/index.html)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues**: Found a bug? [Open an issue](https://github.com/infineon/micropython/issues)
2. **Suggest Features**: Have an idea? Share it in the issues
3. **Submit Pull Requests**: Contribute code improvements
4. **Improve Documentation**: Help make our docs better
5. **Share Examples**: Contribute useful code examples

### Development Setup

```bash
# Clone the repository
git clone https://github.com/infineon/micropython.git
cd micropython

# Follow the build instructions in the repo
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

MicroPython itself is licensed under the MIT License.

## 🔗 Resources

### Community
- **MicroPython Forum**: [forum.micropython.org](https://forum.micropython.org/)
- **Infineon Developer Community**: [community.infineon.com](https://community.infineon.com/)
- **GitHub Discussions**: [github.com/infineon/micropython/discussions](https://github.com/infineon/micropython/discussions)

### Learning Resources
- [MicroPython Official Tutorial](https://docs.micropython.org/en/latest/reference/index.html)
- [PSoC™ 6 Technical Reference Manual](https://www.infineon.com/dgdl/Infineon-PSoC_6_MCU_PSoC_63_with_BLE_Architecture_Technical_Reference_Manual-UserManual-v00_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f946fea01ca)
- [Infineon PSoC™ 6 Product Page](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu/)

### Support
- **Technical Support**: [Infineon Support Portal](https://www.infineon.com/cms/en/about-infineon/company/contacts/support/)
- **Report Bugs**: [GitHub Issues](https://github.com/infineon/micropython/issues)
- **Email**: developer.support@infineon.com

---

## 🎯 Getting Help

If you're stuck:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search [existing issues](https://github.com/infineon/micropython/issues)
3. Ask on the [MicroPython Forum](https://forum.micropython.org/)
4. Create a [new issue](https://github.com/infineon/micropython/issues/new) with:
   - Your board model
   - MicroPython version
   - Complete error messages
   - Steps to reproduce the problem

---

## 🌟 Show Your Support

If you find this project useful:
- ⭐ Star this repository
- 🐛 Report bugs you find
- 📝 Contribute documentation improvements
- 💡 Share your projects built with MicroPython on PSoC™ 6

---

**Happy Coding with MicroPython on PSoC™ 6!** 🐍⚡

<div align="center">
  <sub>Built with ❤️ by the Infineon Team and MicroPython Community</sub>
</div>
