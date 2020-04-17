#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
import spidev
import time

#instacia a classe que usaremos
spi = spidev.SpiDev()
#abre e seta valores ao objeto
spi.open(0, 0)

#metodo que le o valor recebido no CI
def leradc(adcnum):
# le o dado do SPI do MCP3008, que devera estar no intervalo de 8 digitos
# 0 a 7
    if adcnum > 7 or adcnum < 0:
        return -1

#etapa que faz a conversao dos dados lidos de analogico para digital
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    adc_saida = ((r[1] & 3) << 8) + r[2]
    return adc_saida


while True:
    #chama o metodo ler ADC no pino 0 (temos 8 pinos)
    #e atribui o retorno a variavel valor
    valor = leradc(1)
    #verifica a quantos volts equivale a leitura do conversor
    #sendo 0v = 0 Graus Celsius
    #e 3.3v = 100 Graus Clesius
    volts = (valor * 3.3) / 1024
    #converte o valor em volts calculado em temperatura
    temperatura = volts / (10.0 / 1000)
    
    #print ("Valor da leitura%4d/1023 => Volts %5.3f V => Temperatura %4.1f Â°C" % (valor, volts, temperatura))
    print("---------------------------")
    print ("Valor da leitura%4d/1023" % (valor))
    print ("Volts %5.3f V" % (volts))
    print ("Temperatura %4.1f Â°C" % (temperatura))
    print " "


    time.sleep(5)
