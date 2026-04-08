import RPi.GPIO as GPIO
import time, sys
GPI.setmode(GPIO.BOARD)
inpt = 12
GPIO.setup(inpt,GPIO.IN)
rate_cnt = 0
tot_cnt = 0 
minutes = 0
constant = 0.10
time_new = 0.0

print('Fluxo de Agua - Aproximado')
while True:
	time_new = time.time() + 10
	rate_cnt = 0
	while time.time() <= time_new:
		if GPIO.inpt(inpt)!= 0:
			rate_cnt += 1
			tot_cnt += 1
		try:
			print(GPIO.input(inpt), end='')
		except KeyboardInterrupt:
			print('\nCTRL C - Exiting nicely'
			GPIO.cleanup()
			sys.exit()
	minutes += 1
	print('\nLitros por minuto ', round(rate_cnt* constant, 4))
	print('Total de litros ', round(tot_cnt * constant, 4))
	print('Time (minoto e clock) ', minutes, '\t', time.asctime(time)

GPIO.cleanup()
print('Done')
