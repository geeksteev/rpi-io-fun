# This script is to test the functionality of most IO modules. Some IO modules have different default states (On/Off).

import RPi.GPIO as GPIO
import time

output_pin = 21
input_pin = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(output_pin, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def detect_input(pin):
    input=GPIO.input(pin)
    return input

def send_output():
    GPIO.output(output_pin, True)
    GPIO.output(output_pin, False)

try:
    while True:
        if detect_input(input_pin):
            send_output()

except KeyboardInterrupt:
    print("Keyboard interrupted!")
    GPIO.cleanup()
