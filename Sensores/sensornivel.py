#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO 
pino = 16
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(pino, GPIO.IN) 
 
while (True):
    if(GPIO.input(pino) == 1): 
       print "Acima do Nivel"
       time.sleep(1)
    else: 
       print "Abaixo do Nivel"
       time.sleep(1)

