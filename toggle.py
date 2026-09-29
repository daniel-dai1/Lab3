from machine import Pin
import time

button_pins = (22, 10, 11, 12, 13)
led_pins = (16, 17, 18, 20, "LED")

buttons = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in button_pins]
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
led_states = [False] * len(buttons)
last_button_states = [0] * len(buttons)

for led in leds:
    led.off()

while True:
    for index, button in enumerate(buttons):
        current_button_state = button.value()

        if current_button_state and not last_button_states[index]:
            led_states[index] = not led_states[index]
            leds[index].value(led_states[index])
            time.sleep_ms(50)

        last_button_states[index] = current_button_state