
# ~~~  Python program for ist 
#      smart door-lock project  ~~~

# START: Importing Dependencies/Librarys
import speech_recognition as sr
import pyttsx3
import RPi.GPIO as GPIO # Library for servo motor control
from time import sleep # Delays 
import time
# END: Importing Dependencies/Librarys


#initilasing the gpio pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
pwm=GPIO.PWM(8, 50)
pwm.start(0)

#initilasing the gpio pins
GPIO.output(13, GPIO.HIGH)

# unlock varibles
UnlockPhrase = "unlock door"
UnlockPhrase1 = "unlock the door"
UnlockPhrase2 = "porpoise"

# lock varibles
LockPhrase = "lock door"
LockPhrase1 = "lock the door"
LockPhrase2 = "turtle"

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
        
        
# Loop infinitely for user to
# speak

while(1):
        
        # Exception handling to handle
        # exceptions at the runtime
        try:
                
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                        # wait for a second to let the recognizer
                        # adjust the energy threshold based on
                        # the surrounding noise level
                        r.adjust_for_ambient_noise(source2, duration=0.2)
                        #listens for the user's input
                        audio2 = r.listen(source2)
                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()

                        print(time.ctime(time.time()),":", MyText)
                        SpeakText(MyText)


                        # unlock
                        if MyText == UnlockPhrase or MyText == UnlockPhrase1 or MyText == UnlockPhrase2:
                                print("Valid phrase, unlocking now...")
                                
                                def SetAngle(angle):
                                        duty = angle / 18 + 2
                                        GPIO.output(8, True)
                                        pwm.ChangeDutyCycle(duty)
                                        sleep(1)
                                        GPIO.output(8, False)
                                        pwm.ChangeDutyCycle(0)
                                SetAngle(90)

                                

                        

                        # lock
                        if MyText == LockPhrase or MyText == LockPhrase1 or MyText == LockPhrase2:
                                print("Valid phrase, locking now...")
                                
                                def SetAngle(angle):
                                        duty = angle / 18 + 2
                                        GPIO.output(8, True)
                                        pwm.ChangeDutyCycle(duty)
                                        sleep(1)
                                        GPIO.output(8, False)
                                        pwm.ChangeDutyCycle(0)
                                SetAngle(20)


        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
                print("unknown error occured, most likely an unknown phrase or language")