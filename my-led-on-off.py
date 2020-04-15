import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
ledPin1 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.output(ledPin1, GPIO.HIGH)

while True:
    GPIO.output(ledPin1, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(ledPin1, GPIO.LOW)
    time.sleep(0.5)


GPIO.cleanup();
