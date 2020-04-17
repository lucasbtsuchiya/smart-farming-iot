import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(15, GPIO.OUT)
print("LAMPADA DESLIGADA\n")
GPIO.output(15, GPIO.LOW)
