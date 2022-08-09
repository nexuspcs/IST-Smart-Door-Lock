# Testing rgb led on Pi

# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
ledPin = 17 # Broadcom pin 17 



# Pin Setup:
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)


print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.075)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
