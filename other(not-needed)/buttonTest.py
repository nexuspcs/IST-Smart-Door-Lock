import RPi.GPIO as GPIO
import time 

buttonInput = 29
returnGPIOpin = 31
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(returnGPIOpin, GPIO.OUT)

GPIO.output(returnGPIOpin, GPIO.LOW)

while True:
        if GPIO.input(buttonInput) == GPIO.HIGH:
                print("no contact")
                time.sleep(0.2)
        else:
                print("contact")
                time.sleep(0.2)