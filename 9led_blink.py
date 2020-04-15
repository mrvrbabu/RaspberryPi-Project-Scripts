import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

ledPin1 = 3
ledPin2 = 5
ledPin3 = 7

ledPin4 = 11
ledPin5 = 13
ledPin6 = 15

ledPin7 = 18
ledPin8 = 19
ledPin9 = 21

GPIO.setmode(GPIO.BOARD)
# Setup led pin 1 
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.output(ledPin1, GPIO.LOW)
# Setup led pin 2
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.output(ledPin2, GPIO.LOW)
# Setup led pin 3
GPIO.setup(ledPin3, GPIO.OUT)
GPIO.output(ledPin3, GPIO.LOW)

# Setup led pin 4
GPIO.setup(ledPin4, GPIO.OUT)
GPIO.output(ledPin4, GPIO.LOW)

# Setup led pin 5
GPIO.setup(ledPin5, GPIO.OUT)
GPIO.output(ledPin5, GPIO.LOW)

# Setup led pin 6
GPIO.setup(ledPin6, GPIO.OUT)
GPIO.output(ledPin6, GPIO.LOW)

# Setup led pin 6
GPIO.setup(ledPin6, GPIO.OUT)
GPIO.output(ledPin6, GPIO.LOW)

# Setup led pin 7
GPIO.setup(ledPin7, GPIO.OUT)
GPIO.output(ledPin7, GPIO.LOW)


# Setup led pin 8
GPIO.setup(ledPin8, GPIO.OUT)
GPIO.output(ledPin8, GPIO.LOW)

# Setup led pin 9
GPIO.setup(ledPin9, GPIO.OUT)
GPIO.output(ledPin9, GPIO.LOW)


while True:
    GPIO.output(ledPin1, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin1, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin2, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin2, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin3, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin3, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin4, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin4, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin5, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin5, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin6, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin6, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin7, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin7, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin8, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin8, GPIO.LOW)
    time.sleep(0.2)
    
    GPIO.output(ledPin9, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(ledPin9, GPIO.LOW)
    time.sleep(0.2)
    
    
GPIO.cleanup();

