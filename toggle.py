from machine import Pin
import time

# GPIO pins for push buttons and LEDs
button_pins = (22, 10, 11, 12, 13)
led_pins = (16, 17, 18, 20, "LED")

# Initialize button pins as inputs with pull-down resistor
buttons = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in button_pins]
# Initialize LED pin outputs
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
# Track state for each LED
led_states = [False] * len(buttons)
# Store previous state of button for edge detection
last_button_states = [0] * len(buttons)

# Ensures all LEDs start in OFF state
for led in leds:
    led.off()

# Main program Loop
while True:
    # Iterate through all buttons with their corresponding index
    for index, button in enumerate(buttons):
        current_button_state = button.value()

        # Detect rising edge
        if current_button_state and not last_button_states[index]:
            # Toggle the state of the corresponding LED
            led_states[index] = not led_states[index]
            leds[index].value(led_states[index])
            # Delay for software debounce
            time.sleep_ms(50)
        # Updates the previous state for the next loop item
        last_button_states[index] = current_button_state
