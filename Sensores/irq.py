# -*- coding: utf-8 -*-
#!/usr/bin/env python
import RPi.GPIO as gpio
#definir a funcao de callback
def gpio_callback(gpio_id, value):
   print("Deu certo")

#adicionar a interrupcao
RPIO.add_interrupt_callback(23, gpio_callback, edge='falling', pull_up_down=RPIO.PUD_UP, threaded_callback=True, debounce_timeout_ms=0)
#colocar a interrupcao em loop
input()
RPIO.wait_for_interrupts()