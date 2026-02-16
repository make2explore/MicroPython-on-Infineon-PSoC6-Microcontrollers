"""
Timer and Interrupt Example for PSoC™ 6 MicroPython

This example demonstrates using timers and interrupts for:
- Periodic task execution
- Precise timing without blocking
- Hardware timer callbacks
- External interrupt handling (button press)

Timers allow executing code at regular intervals without blocking
the main program, making them essential for real-time applications.

Interrupts allow responding immediately to external events (button press,
sensor trigger, etc.) instead of constantly polling.
"""

from machine import Pin, Timer
import time

print("Timer and Interrupt Example for PSoC™ 6")
print("=" * 50)

# Configuration
LED_PIN = 'P13_7'
BUTTON_PIN = 'P0_4'

# Initialize LED
led = Pin(LED_PIN, Pin.OUT)
led.off()

# Counter for demonstrations
tick_count = 0
button_press_count = 0

# =========================================================================
# Example 1: Software Timer (Periodic Callback)
# =========================================================================
print("\nExample 1: Periodic Timer (5 seconds)")
print("LED will blink automatically using a timer")

def timer_callback(timer):
    """Called automatically by the timer"""
    global tick_count
    led.toggle()
    tick_count += 1
    print(f"  Timer tick {tick_count}: LED toggled")

# Create timer that triggers every 500ms
timer1 = Timer(0)
timer1.init(period=500, mode=Timer.PERIODIC, callback=timer_callback)

# Let it run for 5 seconds
time.sleep(5)

# Stop the timer
timer1.deinit()
print(f"Timer stopped after {tick_count} ticks")
led.off()
tick_count = 0

# =========================================================================
# Example 2: One-Shot Timer
# =========================================================================
print("\nExample 2: One-Shot Timer")
print("LED will turn on after 2 seconds")

def one_shot_callback(timer):
    """Called once after the delay"""
    led.on()
    print("  One-shot timer fired! LED is ON")

led.off()
timer2 = Timer(1)
timer2.init(period=2000, mode=Timer.ONE_SHOT, callback=one_shot_callback)

# Wait for the timer to fire
time.sleep(3)
led.off()
timer2.deinit()

# =========================================================================
# Example 3: Multiple Timers
# =========================================================================
print("\nExample 3: Multiple Timers Running Simultaneously (5 seconds)")

fast_count = 0
slow_count = 0

def fast_timer_callback(timer):
    """Fast timer: 200ms"""
    global fast_count
    fast_count += 1
    print(f"  Fast: {fast_count}")

def slow_timer_callback(timer):
    """Slow timer: 1000ms"""
    global slow_count
    slow_count += 1
    led.toggle()
    print(f"  Slow: {slow_count} (LED toggled)")

# Create two timers with different periods
fast_timer = Timer(0)
slow_timer = Timer(1)

fast_timer.init(period=200, mode=Timer.PERIODIC, callback=fast_timer_callback)
slow_timer.init(period=1000, mode=Timer.PERIODIC, callback=slow_timer_callback)

# Let both run
time.sleep(5)

# Clean up
fast_timer.deinit()
slow_timer.deinit()
led.off()
print(f"Fast timer: {fast_count} ticks, Slow timer: {slow_count} ticks")

# =========================================================================
# Example 4: External Interrupt (Button Press)
# =========================================================================
print("\nExample 4: External Interrupt on Button Press")
print("Press the button (or connect pin to GND) to trigger interrupt")

def button_callback(pin):
    """Called when button is pressed"""
    global button_press_count
    button_press_count += 1
    led.toggle()
    print(f"  Button pressed! Count: {button_press_count}")

# Configure button with pull-up (active low)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

# Set up interrupt on falling edge (button press)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

print("Interrupt enabled. Waiting for button presses (10 seconds)...")
time.sleep(10)

# Disable interrupt
button.irq(handler=None)
print(f"Button was pressed {button_press_count} times")
led.off()

# =========================================================================
# Example 5: Rising and Falling Edge Interrupts
# =========================================================================
print("\nExample 5: Both Rising and Falling Edge Interrupts")
print("Detecting both button press and release")

press_count = 0
release_count = 0

def button_press_callback(pin):
    """Called on falling edge (press)"""
    global press_count
    press_count += 1
    led.on()
    print(f"  Button PRESSED (count: {press_count})")

def button_release_callback(pin):
    """Called on rising edge (release)"""
    global release_count
    release_count += 1
    led.off()
    print(f"  Button RELEASED (count: {release_count})")

# Note: MicroPython typically supports only one interrupt per pin
# This example shows the concept - implementation may vary
button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, 
           handler=lambda p: button_press_callback(p) if p.value() == 0 
                           else button_release_callback(p))

print("Press and release the button (10 seconds)...")
time.sleep(10)

button.irq(handler=None)
print(f"Presses: {press_count}, Releases: {release_count}")

# =========================================================================
# Example 6: Timer for Periodic Task (Non-blocking)
# =========================================================================
print("\nExample 6: Non-blocking Periodic Task with Timer")
print("Main loop continues while timer handles LED blinking")

def blink_callback(timer):
    """Blink LED in background"""
    led.toggle()

# Start background timer
blink_timer = Timer(0)
blink_timer.init(period=200, mode=Timer.PERIODIC, callback=blink_callback)

# Main loop can do other work
print("Main loop running while LED blinks in background...")
for i in range(10):
    print(f"  Main loop iteration {i+1}")
    # Simulate other work
    time.sleep(0.5)

# Stop background task
blink_timer.deinit()
led.off()
print("Background blinking stopped")

# =========================================================================
# Example 7: Watchdog-like Timer
# =========================================================================
print("\nExample 7: Timeout Detection with Timer")

timeout_occurred = False

def timeout_callback(timer):
    """Called if timeout occurs"""
    global timeout_occurred
    timeout_occurred = True
    print("  TIMEOUT! System not responding")

# Create watchdog-style timer (5 second timeout)
watchdog = Timer(2)
watchdog.init(period=5000, mode=Timer.ONE_SHOT, callback=timeout_callback)

# Simulate normal operation (reset timer before timeout)
print("Simulating normal operation...")
for i in range(3):
    print(f"  Working... {i+1}")
    time.sleep(1)
    # Reset the timer (feed the watchdog)
    watchdog.deinit()
    watchdog.init(period=5000, mode=Timer.ONE_SHOT, callback=timeout_callback)

print("  All tasks completed normally")
watchdog.deinit()

# Now simulate a timeout
print("\nSimulating system hang (no timer reset)...")
watchdog.init(period=2000, mode=Timer.ONE_SHOT, callback=timeout_callback)
time.sleep(3)  # Don't reset timer - let it timeout

if timeout_occurred:
    print("Timeout was detected and handled")
    
watchdog.deinit()

print("\n" + "=" * 50)
print("Timer and Interrupt examples completed")
led.off()

"""
Timer Modes:
- Timer.ONE_SHOT: Fires once after specified period
- Timer.PERIODIC: Fires repeatedly at specified intervals

Timer Functions:
- timer.init(period, mode, callback) - Initialize and start timer
- timer.deinit() - Stop and disable timer
- period is in milliseconds

Interrupt Triggers:
- Pin.IRQ_FALLING: Trigger on high-to-low transition
- Pin.IRQ_RISING: Trigger on low-to-high transition
- Pin.IRQ_FALLING | Pin.IRQ_RISING: Trigger on both edges

Interrupt Functions:
- pin.irq(trigger, handler) - Set up interrupt
- pin.irq(handler=None) - Disable interrupt

Best Practices:
1. Keep interrupt handlers SHORT and FAST
2. Don't use blocking operations in interrupts (no sleep!)
3. Don't print extensively in interrupts (can cause issues)
4. Use flags to communicate between interrupts and main code
5. Consider debouncing for mechanical buttons
6. Always clean up (deinit) timers when done

Common Use Cases:
- Periodic sensor readings without blocking
- LED blinking while doing other tasks
- Button press detection
- Timeout detection
- Event counting
- PWM generation (though hardware PWM is better)
- Scheduling multiple tasks

Debouncing Example:
For mechanical buttons, add a small delay or use a timer
to ignore multiple rapid triggers caused by button bounce.
"""

# Helper function for debouncing (example)
def debounced_button_handler(pin):
    """Button handler with simple debounce"""
    # Disable interrupt temporarily
    pin.irq(handler=None)
    
    # Your button handling code here
    led.toggle()
    print("Debounced button press")
    
    # Re-enable after delay
    time.sleep_ms(200)  # 200ms debounce time
    pin.irq(trigger=Pin.IRQ_FALLING, handler=debounced_button_handler)
