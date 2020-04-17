# -*- coding: utf-8 -*-
#! /usr/bin/python
 
import RPi.GPIO as gpio
import time
 
""" Global """
PIN=23
pi = 3.14159265
periodo = 5000
delaytime = 2000
raio = 147
amostra = 0
global contador
contador = 0
rmp = 0
metro_segundo = 0
km_hora = 0


""" Funcoes """
def millis():
    return time.time() * 1000

def interrupcao(gpio_pin):
    global contador
    contador = contador + 1

def velocidade_vento():
    
    metro_segundo = 0
    km_hora = 0
    contador = 0;
    interrupcao(PIN)
    millis()
    start_time = millis()
    while(millis() < (start_time + periodo)):
        print ("Oi")

def RPMcalc():
    rpm = ((contador*60)/(periodo/1000))
    metro_segundo = ((4 * pi * raio * rpm)/60)/1000
    km_hora = (((4 * pi * raio * rpm)/60)/1000)*3.6


""" Configurando GPIO """
# Configurando o modo dos pinos como BCM
gpio.setmode(gpio.BCM) 
 
# Configurando PIN como INPUT e modo pull-donw interno
gpio.setup(PIN, gpio.IN, pull_up_down = gpio.PUD_DOWN)
 
# Adicionando um evento ao GPIO 23 na mudança RISING 0V[LOW] - > 3.3V[HIGH]
gpio.add_event_detect(PIN, gpio.RISING)
 
while True:

    velocidade_vento()
    print('Velocidade em m/s', metro_segundo)
    time.sleep(1)
 