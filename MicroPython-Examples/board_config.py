"""
Board Configuration File for PSoC™ 6 MicroPython

This file contains pin configurations for different PSoC™ 6 boards.
Import the appropriate configuration for your board to avoid hardcoding
pin numbers in your code.

Usage:
    from board_config import BOARD_CY8CPROTO_062_4343W as board
    led = Pin(board.LED, Pin.OUT)
"""

class BoardConfig:
    """Base board configuration class"""
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"<BoardConfig: {self.name}>"

# =========================================================================
# CY8CPROTO-062-4343W - PSoC™ 6 Wi-Fi BT Prototyping Kit
# =========================================================================
class CY8CPROTO_062_4343W(BoardConfig):
    """
    CY8CPROTO-062-4343W Board Configuration
    Features: Wi-Fi 802.11bgn, Bluetooth 5.0, Arduino headers
    """
    def __init__(self):
        super().__init__("CY8CPROTO-062-4343W")
        
        # LEDs
        self.LED = 'P13_7'          # User LED (Red)
        self.LED_RED = 'P13_7'      # Same as LED
        
        # Buttons
        self.BUTTON = 'P0_4'        # User button SW2
        self.SW2 = 'P0_4'           # Same as BUTTON
        
        # I2C
        self.I2C0_SDA = 'P6_1'
        self.I2C0_SCL = 'P6_0'
        
        # SPI
        self.SPI0_MOSI = 'P12_0'
        self.SPI0_MISO = 'P12_1'
        self.SPI0_SCK = 'P12_2'
        
        # UART
        self.UART0_TX = 'P5_1'
        self.UART0_RX = 'P5_0'
        
        # ADC
        self.A0 = 'P10_0'           # Arduino A0
        self.A1 = 'P10_1'           # Arduino A1
        self.A2 = 'P10_2'           # Arduino A2
        self.A3 = 'P10_3'           # Arduino A3
        self.A4 = 'P10_4'           # Arduino A4
        self.A5 = 'P10_5'           # Arduino A5

# Create instance for easy import
BOARD_CY8CPROTO_062_4343W = CY8CPROTO_062_4343W()

# =========================================================================
# CY8CPROTO-063-BLE - PSoC™ 6 BLE Prototyping Kit
# =========================================================================
class CY8CPROTO_063_BLE(BoardConfig):
    """
    CY8CPROTO-063-BLE Board Configuration
    Features: Bluetooth Low Energy 5.0
    """
    def __init__(self):
        super().__init__("CY8CPROTO-063-BLE")
        
        # LEDs
        self.LED = 'P6_3'           # User LED (Orange)
        self.LED_ORANGE = 'P6_3'    # Same as LED
        
        # Buttons
        self.BUTTON = 'P0_4'        # User button SW2
        self.SW2 = 'P0_4'
        
        # I2C
        self.I2C0_SDA = 'P6_1'
        self.I2C0_SCL = 'P6_0'
        
        # SPI
        self.SPI0_MOSI = 'P12_0'
        self.SPI0_MISO = 'P12_1'
        self.SPI0_SCK = 'P12_2'
        
        # UART
        self.UART0_TX = 'P5_1'
        self.UART0_RX = 'P5_0'
        
        # ADC
        self.A0 = 'P10_0'
        self.A1 = 'P10_1'
        self.A2 = 'P10_2'
        self.A3 = 'P10_3'

# Create instance
BOARD_CY8CPROTO_063_BLE = CY8CPROTO_063_BLE()

# =========================================================================
# CY8CKIT-062-BLE - PSoC™ 6 BLE Pioneer Kit
# =========================================================================
class CY8CKIT_062_BLE(BoardConfig):
    """
    CY8CKIT-062-BLE Board Configuration
    Features: BLE, CapSense, Arduino headers
    """
    def __init__(self):
        super().__init__("CY8CKIT-062-BLE")
        
        # LEDs
        self.LED = 'P13_7'          # User LED (Orange)
        self.LED_ORANGE = 'P13_7'
        self.LED_RED = 'P1_5'       # RGB LED - Red
        self.LED_GREEN = 'P0_5'     # RGB LED - Green
        self.LED_BLUE = 'P1_1'      # RGB LED - Blue
        
        # Buttons
        self.BUTTON = 'P0_4'        # User button SW2
        self.SW2 = 'P0_4'
        
        # I2C
        self.I2C0_SDA = 'P6_1'
        self.I2C0_SCL = 'P6_0'
        
        # SPI
        self.SPI0_MOSI = 'P12_0'
        self.SPI0_MISO = 'P12_1'
        self.SPI0_SCK = 'P12_2'
        
        # UART
        self.UART0_TX = 'P5_1'
        self.UART0_RX = 'P5_0'
        
        # ADC
        self.A0 = 'P10_0'
        self.A1 = 'P10_1'
        self.A2 = 'P10_2'
        self.A3 = 'P10_3'
        self.A4 = 'P10_4'
        self.A5 = 'P10_5'

# Create instance
BOARD_CY8CKIT_062_BLE = CY8CKIT_062_BLE()

# =========================================================================
# CY8CKIT-062-WIFI-BT - PSoC™ 6 Wi-Fi BT Pioneer Kit
# =========================================================================
class CY8CKIT_062_WIFI_BT(BoardConfig):
    """
    CY8CKIT-062-WIFI-BT Board Configuration
    Features: Wi-Fi, Bluetooth, Arduino headers
    """
    def __init__(self):
        super().__init__("CY8CKIT-062-WIFI-BT")
        
        # LEDs
        self.LED = 'P13_7'          # User LED (Orange)
        self.LED_ORANGE = 'P13_7'
        self.LED_RED = 'P1_5'       # RGB LED - Red
        self.LED_GREEN = 'P0_5'     # RGB LED - Green
        self.LED_BLUE = 'P1_1'      # RGB LED - Blue
        
        # Buttons
        self.BUTTON = 'P0_4'        # User button SW2
        self.SW2 = 'P0_4'
        
        # I2C
        self.I2C0_SDA = 'P6_1'
        self.I2C0_SCL = 'P6_0'
        
        # SPI
        self.SPI0_MOSI = 'P12_0'
        self.SPI0_MISO = 'P12_1'
        self.SPI0_SCK = 'P12_2'
        
        # UART
        self.UART0_TX = 'P5_1'
        self.UART0_RX = 'P5_0'
        
        # ADC
        self.A0 = 'P10_0'
        self.A1 = 'P10_1'
        self.A2 = 'P10_2'
        self.A3 = 'P10_3'
        self.A4 = 'P10_4'
        self.A5 = 'P10_5'

# Create instance
BOARD_CY8CKIT_062_WIFI_BT = CY8CKIT_062_WIFI_BT()

# =========================================================================
# CY8CKIT-062S2-43012 - PSoC™ 62S2 Wi-Fi BT Pioneer Kit
# =========================================================================
class CY8CKIT_062S2_43012(BoardConfig):
    """
    CY8CKIT-062S2-43012 Board Configuration
    Features: Wi-Fi, Bluetooth, Secure Boot
    """
    def __init__(self):
        super().__init__("CY8CKIT-062S2-43012")
        
        # LEDs
        self.LED = 'P13_7'          # User LED (Orange)
        self.LED_ORANGE = 'P13_7'
        self.LED_RED = 'P1_5'       # RGB LED - Red
        self.LED_GREEN = 'P11_1'    # RGB LED - Green
        self.LED_BLUE = 'P1_1'      # RGB LED - Blue
        
        # Buttons
        self.BUTTON = 'P0_4'        # User button SW2
        self.SW2 = 'P0_4'
        
        # I2C
        self.I2C0_SDA = 'P6_1'
        self.I2C0_SCL = 'P6_0'
        
        # SPI
        self.SPI0_MOSI = 'P12_0'
        self.SPI0_MISO = 'P12_1'
        self.SPI0_SCK = 'P12_2'
        
        # UART
        self.UART0_TX = 'P5_1'
        self.UART0_RX = 'P5_0'
        
        # ADC
        self.A0 = 'P10_0'
        self.A1 = 'P10_1'
        self.A2 = 'P10_2'
        self.A3 = 'P10_3'
        self.A4 = 'P10_4'
        self.A5 = 'P10_5'

# Create instance
BOARD_CY8CKIT_062S2_43012 = CY8CKIT_062S2_43012()

# =========================================================================
# Helper Functions
# =========================================================================

def list_boards():
    """List all available board configurations"""
    boards = [
        BOARD_CY8CPROTO_062_4343W,
        BOARD_CY8CPROTO_063_BLE,
        BOARD_CY8CKIT_062_BLE,
        BOARD_CY8CKIT_062_WIFI_BT,
        BOARD_CY8CKIT_062S2_43012
    ]
    
    print("Available PSoC™ 6 Board Configurations:")
    print("-" * 50)
    for i, board in enumerate(boards, 1):
        print(f"{i}. {board.name}")
    print("-" * 50)
    return boards

def detect_board():
    """
    Attempt to detect the current board (placeholder)
    In practice, this would need board-specific detection logic
    """
    import sys
    print(f"Platform: {sys.platform}")
    print("Note: Automatic board detection not yet implemented")
    print("Please manually select your board configuration")
    return None

# =========================================================================
# Usage Examples
# =========================================================================

if __name__ == '__main__':
    print("PSoC™ 6 Board Configuration Module\n")
    
    # List all available boards
    list_boards()
    
    # Example: Using specific board configuration
    print("\nExample: Using CY8CPROTO-062-4343W configuration")
    board = BOARD_CY8CPROTO_062_4343W
    print(f"Board: {board.name}")
    print(f"LED Pin: {board.LED}")
    print(f"Button Pin: {board.BUTTON}")
    print(f"I2C SDA: {board.I2C0_SDA}, SCL: {board.I2C0_SCL}")
    
    # Example: LED control using board config
    print("\nExample: LED control with board configuration")
    print("from machine import Pin")
    print("from board_config import BOARD_CY8CPROTO_062_4343W as board")
    print("led = Pin(board.LED, Pin.OUT)")
    print("led.on()")

"""
Board Configuration Best Practices:

1. Always use board configuration instead of hardcoded pins:
   GOOD: led = Pin(board.LED, Pin.OUT)
   BAD:  led = Pin('P13_7', Pin.OUT)

2. Import the configuration at the top of your code:
   from board_config import BOARD_CY8CPROTO_062_4343W as board

3. This makes your code portable across different boards
   Just change the import line to switch boards

4. Add custom pins to your local configuration:
   board.MY_SENSOR = 'P9_0'
   sensor = Pin(board.MY_SENSOR, Pin.IN)

5. Refer to your board's schematic for available pins
"""
