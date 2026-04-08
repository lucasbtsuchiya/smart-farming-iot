# -*- coding: utf-8 -*-
from gpiozero import MCP3008
from time import sleep
higro = MCP3008(1) # Atribui o canal 1 para esta leitura

while True:
      # Normalizei a escala onde 0 é completamente seco 
      # e 100 é completamente molhado
      higro_perc = (1 - higro.value) * 100
      tensao = (higro.value * 5.0) / 255.0
      print('Valor lido:', higro.value)
      print('Tensao no pino:', tensao)
      print('Umidade do Solo {0}%',higro_perc)
      sleep(1)   # executa 1 leitura nova a cada segundo


