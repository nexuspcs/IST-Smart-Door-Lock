# Testing rgb led on Pi

# External module imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin Definitons:
ledPin = 17 # Broadcom pin 23 (P1 pin 16)



# Pin Setup:
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(ledPin, GPIO.HIGH)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO