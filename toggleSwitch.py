#::START::#
# AUTHOR: JAMES COATES - 2022 # 
# ~~~  Python program for ist 
#      smart door-lock project  ~~~

# START: Importing Dependencies/Librarys
import RPi.GPIO as GPIO
import time 
from time import sleep 
# END: Importing Dependencies/Librarys


buttonInput = 29 # 
returnGPIOpin = 31
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buttonInput, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(returnGPIOpin, GPIO.OUT)

GPIO.output(returnGPIOpin, GPIO.LOW)



GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwm=GPIO.PWM(8, 50)
pwm.start(0)




ledPinRed = 11
GPIO.setup(ledPinRed, GPIO.OUT)
ledPinGreen = 23
GPIO.setup(ledPinGreen, GPIO.OUT)

GPIO.output(ledPinRed, GPIO.HIGH)
GPIO.output(ledPinGreen, GPIO.HIGH)



# initilasing the servo motor
GPIO.output(13, GPIO.HIGH)





while True:
        if GPIO.input(buttonInput) == GPIO.HIGH:
                print("GPIO is high, so will unlock")
                time.sleep(0.2)
        if GPIO.input(buttonInput) == GPIO.LOW:
                print("GPIO is low, so will lock")
                # push button down = unlock
                GPIO.output(ledPinGreen, GPIO.LOW)
                GPIO.output(ledPinRed, GPIO.HIGH)
                                
                # some simple math for Pulse width Modulation 
                def SetAngle(angle):
                        duty = angle / 18 + 2
                        GPIO.output(8, True)
                        pwm.ChangeDutyCycle(duty)
                        sleep(1)
                        GPIO.output(8, False)
                        pwm.ChangeDutyCycle(0)
                SetAngle(90)




                
        else:
                print("no switch position, dormant")