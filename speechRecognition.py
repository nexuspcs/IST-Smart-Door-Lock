#::START::#
# AUTHOR: JAMES COATES - 2022 # 
# ~~~  Python program for ist 
#      smart door-lock project  ~~~

# START: Importing Dependencies/Librarys
import speech_recognition as sr
import pyttsx3
import RPi.GPIO as GPIO # Library for servo motor control and LEDs
from time import sleep # Delays 
import time
# END: Importing Dependencies/Librarys


# initilasing the gpio pins
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


# unlock varibles
UnlockPhrase = "unlock door"
UnlockPhrase1 = "unlock the door"
UnlockPhrase2 = "porpoise"


# lock varibles
LockPhrase = "lock door"
LockPhrase1 = "lock the door"
LockPhrase2 = "turtle"


# Initialising the recogniser
r = sr.Recognizer()


# Function to convert text to speech
def SpeakText(command):
        # Initialise the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        
        
# Loop infinitely for user to speak (a.k.a waiting for user input) 
while(1):
        
        # Exception handling to handle exceptions at/with the runtime
        try:
                
                # Use the microphone as source for input.
                with sr.Microphone() as source2:
                        # wait for a second to let the recogniser
                        # adjust the energy threshold based on
                        # the surrounding noise level (a.k.a noise reduction)
                        r.adjust_for_ambient_noise(source2, duration=0.2)
                        #listens for the user's input
                        audio2 = r.listen(source2)
                        # Using google's **local** libary, on the Pi to recognise audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()

                        print(time.ctime(time.time()),":", MyText)
                        SpeakText(MyText)


                        # unlock function 
                        if MyText == UnlockPhrase or MyText == UnlockPhrase1 or MyText == UnlockPhrase2:
                                print("Valid phrase, unlocking now...")
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


                        # lock function
                        if MyText == LockPhrase or MyText == LockPhrase1 or MyText == LockPhrase2:
                                print("Valid phrase, locking now...")
                                GPIO.output(ledPinGreen, GPIO.HIGH)
                                GPIO.output(ledPinRed, GPIO.LOW)
                                
                                # some simple math for Pulse width Modulation 
                                def SetAngle(angle):
                                        duty = angle / 18 + 2
                                        GPIO.output(8, True)
                                        pwm.ChangeDutyCycle(duty)
                                        sleep(1)
                                        GPIO.output(8, False)
                                        pwm.ChangeDutyCycle(0)
                                SetAngle(20)


        # if libs unavailable during processing, print error message
        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

        # if unable to recgonise audio/user input, print error message
        except sr.UnknownValueError:
                print("unknown error occured, most likely an unknown phrase or language")
    
        except KeyboardInterrupt:
                GPIO.output(ledPinRed, GPIO.HIGH)
                GPIO.output(ledPinGreen, GPIO.HIGH)
                exit()
#::END::#
# ~~~  Python program for ist 
#      smart door-lock project  ~~~