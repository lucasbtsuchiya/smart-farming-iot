#!/usr/bin/python
from gpiozero import MCP3008
from time import sleep
import sys
pot = MCP3008(0)
tensao = MCP3008(0)
while True:
         print (pot.value)
	 print(tensao.value)
	 sleep(0.5)
