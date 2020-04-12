import RPi.GPIO as GPIO     # Use GPIO Library
import time                 # Import time

buttonPin = 16              # Set pin number 16 to connected to press button switch while pin number 14 connected to GND
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # set buttonPin as input and enable pullup resistor

while True:
    input_state = GPIO.input(buttonPin)    # Retrieve the stage of the button pin
    if (input_state) == False:
        print( 'Button Pressed ...... ')    # Display button pressed
        time.sleep(0.3)                     # Wait for 0.3 seconds for debouncing


GPIO.cleanup();                             # Clean up when exiting the program



