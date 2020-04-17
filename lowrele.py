import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40, GPIO.OUT)
print("LAMPADA DESLIGADA\n")
GPIO.output(40, GPIO.LOW)
