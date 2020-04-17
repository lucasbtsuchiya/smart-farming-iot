#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import subprocess 
import re 
import os 
import time
import MySQLdb as mdb 
import datetime
from gpiozero import MCP3008
from time import sleep
from BMP180 import BMP180
import Adafruit_DHT

databaseUsername="root"
databasePassword="mysqlnet" 
databaseName="irriga" #do not change unless you named the Wordpress database with some other name

#sensor=Adafruit_DHT.DHT22 #if not using DHT22, replace with Adafruit_DHT.DHT11 or Adafruit_DHT.AM2302
canalldr = 0
canal=1 #if not using pin number 4, change here
canalchuva = 2
canalnivel = 3
bmp = BMP180()
sensor=Adafruit_DHT.DHT22 #if not using DHT22, replace with Adafruit_DHT.DHT11 or Adafruit_DHT.AM2302
pinNum=17 #if not using pin number 4, change here



def sensorta():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius

def saveToDatabase(luminosidade, humidadesolo, chuva, pressao, altitude, temperatura, humidade, temp, ph, fluxo, nivel, acionamento):

        con=mdb.connect("localhost", databaseUsername, databasePassword, databaseName)
        currentDate=datetime.datetime.now().date()
        now=datetime.datetime.now()
        midnight=datetime.datetime.combine(now.date(),datetime.time())
        minutes=((now-midnight).seconds)/60 #minutes after midnight, use datead$

        
        with con:
                cur=con.cursor()
                
                cur.execute("INSERT INTO sensores (luminosidade, humidadesolo, chuva, pressao, altitude, temperatura, humidade, temp, ph, fluxo, nivel, acionamento, dateMeasured, hourMeasured) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(luminosidade, humidadesolo, chuva, pressao, altitude, temperatura, humidade, temp, ph, fluxo, nivel, acionamento, currentDate, minutes))
                print 'Dados inseridos!'
                return "true"


def readInfo():
        # Leitura do canal 0 definido para o sensor de luz no Conversor AD
        readldr = MCP3008(canalldr)
        luminosidade = (1 - readldr.value) * 100
        luminosidade = round(luminosidade,3)
        print "Luminosidade em %.2f" % luminosidade
    
        # Leitura do canal 1 definido para o sensor de humidade do solo no Conversor AD
        reads = MCP3008(canal)
        humidadesolo = (1 - reads.value) * 100
        humidadesolo = round(humidadesolo, 2)
        print"Umidade do Solo em %.2f" % humidadesolo
              
        # Leitura do canal 1 definido para o sensor de detecção de chuva no Conversor AD
        readchuva = MCP3008(canalchuva)
        readchuva = (1 - readchuva.value) * 100
        readchuva = round(readchuva, 2)
        print"Chuva: %.2f" % readchuva
        if (readchuva <= 0.8):
                print "Não esta Chovendo %.2f" % readchuva
                chuva = "Nao"
        else:
                print "Chovendo %.2f" % readchuva
                chuva = "Chovendo"
              
        #Leitura do sensor de pressão
        readpressao = bmp.read_pressure()
        pressao = readpressao / 100.0  
        print "Pressao:    %.2f hPa" % pressao
        altitude = bmp.read_altitude()
        altitude = round(altitude, 2);
        print "Altitude:     %.2f m" % altitude
              
        #Leitura do sendor de temperatura e humidade
        humidade, temperature = Adafruit_DHT.read_retry(sensor, pinNum)#read_retry - retry getting temperatures for 15 times
        temperature = round(temperature, 2);
        humidade = round(humidade, 2);
        print "Temperatura: %.1f C" % temperature
        print "Humidade:    %.2f " % humidade 
        
        # Leitura do sensor de temperatura da água
        serialNum = sensorta()
        temp = read(serialNum) 
        print "Temperatura Agua: %.2f C" % temp
        
        ph = 0
        fluxo = 0
        acionamento = 0
        
        readnivel = MCP3008(canalnivel)
        if (readnivel.value == 1):
                print 'Acima do nivel', readnivel.value
                nivel = "Acima do Nivel"
        else:
                print 'Abaixo do nivel', readnivel.value
                nivel = "Abaixo do Nivel"
        
        return saveToDatabase(luminosidade, humidadesolo, chuva, pressao, altitude, temperature, humidade, temp, ph, fluxo, nivel, acionamento)
        #print "Temperature: %.1f C" % temperature
        #print "Humidity:    %s %%" % humidity

        #if humidity is not None and temperature is not None:
                 #success, save the readings
        #else:
                #print 'Failed to get reading. Try again!'
                #sys.exit(1)


#check if table is created or if we need to create one
try:
        queryFile=file("createTable.sql","r")

        con=mdb.connect("localhost", databaseUsername,databasePassword,databaseName)
        currentDate=datetime.datetime.now().date()

        with con:
                line=queryFile.readline()
                query=""
                while(line!=""):
                        query+=line
                        line=queryFile.readline()
                
                cur=con.cursor()
                cur.execute(query)      

                #now rename the file, because we do not need to recreate the table everytime this script is run
                queryFile.close()
                os.rename("createTable.sql","createTable.sql.bkp")
        

except IOError:
        pass #table has already been created
        

status=readInfo() #get the readings


