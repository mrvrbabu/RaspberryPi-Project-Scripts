import RPi.GPIO as GPIO    # Use GPIO library
import time     # Use time library

GPIO.setwarnings(False)

ledPin1 = 11    # Set pin 11 as led anode output pin
ledPin2 = 13    # Set pin 13 as another led anode output pin

GPIO.setmode(GPIO.BOARD)    # Nubers GPIOs by physical location
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.output(ledPin1, GPIO.HIGH)

GPIO.setup(ledPin2, GPIO.OUT)
GPIO.output(ledPin2, GPIO.HIGH)

while True:   # set condition
    GPIO.output(ledPin1, GPIO.HIGH)
    time.sleep(0.5)    # Pause for the given seconds/msecs
    GPIO.output(ledPin1, GPIO.LOW)
    time.sleep(0.5)     # Pause for the given seconds/msecs
    GPIO.output(ledPin2, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(ledPin2, GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup();   #Clean up when exiting the program

