# This script captures an image with the Raspberry Pi Infrared Camera when the touch sensor is tapped.
# Hardware and Wiring: 
#   1. Raspberry Pi 3 Model B v2
#   2. Infrared Camera (attached via ZIF connection on RPi board)
#   3. Keyes Touch Sensor:
#       GND --> GPIO Ground
#       VCC --> GPIO 3V3 Power
#         S --> GPIO 17
#   4. Keyes 4-PIN RGB LED (attached to Ground and GPIO 21). I didn't use all 3 colors, only green.
#         B --> n/a
#         G --> GPIO 21
#         R --> n/a
#         - --> Ground

# Default Imports
import time
# Non-default imports (requires installation via pip3)
import RPi.GPIO as GPIO     
from picamera2 import Picamera2

# Variables
output_pin = 21     # I set these as human readable so as you go through the code its easier to understand.
input_pin = 17      # The numbers correlate with the GPIO pins that each device is plugged into.
img_name = time.strftime("%Y%m%d-%H%M%S") + ".jpg"   # Set the output filename to a date timestamp to remove the possibility of issues with overwriting existing files.

# GPIO Setup
GPIO.setwarnings(False)     # This is optional. Disable warnings, they tend to be a bit verbose.
GPIO.setmode(GPIO.BCM)      # Set the GPIO mode. There are two modes that I'm aware of (BOARD and BCM). I don't fully understand this yet.

# GPIO Device Configuration
# The GPIO configuration is binary. GPIO.OUT sets the device as an output and GPIO.IN sets the device as an input.
# I've found that most inputs require the pull_up_down option to be set. I need to learn more about this.
GPIO.setup(output_pin, GPIO.OUT)    
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Camera Setup
picam2 = Picamera2()
still_config = picam2.create_still_configuration()
picam2.configure(still_config)

# Definitions
def capture_image(img_name):    # Captures an image. 
    picam2.start()
    picam2.capture_file(img_name)
    picam2.stop()

def detect_input(pin):      # Detects input from whatever input device you're using.
    input=GPIO.input(pin)
    return input

def send_output():      # Sends output from whatever output device you're using.
    GPIO.output(output_pin, True)
    time.sleep(0.1)
    GPIO.output(output_pin, False)

try:
    while True:
        if detect_input(input_pin): 
            capture_image(img_name) 
            send_output()

except KeyboardInterrupt:   
    GPIO.cleanup()  # This resets the GPIO pins to their unconfigured state so devices don't continue to run after stopping the program.
    exit()