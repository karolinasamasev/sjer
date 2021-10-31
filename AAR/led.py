#Import
import RPi.GPIO as GPIO
import time

#BCM or baoard
GPIO.setmode(GPIO.BOARD)
#to disable warnings
GPIO.setwarnings(False)

#set gpio... as an output
GPIO.setup(37, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Definitsioonid
def lülita_sisse(tulukene):
    GPIO.output(tulukene, GPIO.HIGH)

def lülita_välja(tulukene):
    GPIO.output(tulukene, GPIO.LOW)

def vilgub(tulukene):
    for i in range(3):
        lülita_sisse(tulukene)
        time.sleep(1/3)
        lülita_välja(tulukene)
        time.sleep(1/3)
sininee = 0
roheline=0
def nupuvajutus(channel):
    global sininee
    sininee = 1
    lülita_sisse(sinine)

#Muutujad
punane_jalakaijad=37
punane_auto=18
kollane=22
roheline_auto=11
roheline_jalakaijad=31
sinine=36
nupp=16

#Nupuvajutuse ootamine
GPIO.add_event_detect(16, GPIO.RISING, callback=nupuvajutus)
lülita_sisse(punane_jalakaijad)

def ajavott():
    aeg=time.time()
    muutuja
    while muutuja==aeg+5:
        muutuja=time.time()
        if GPIO.input(tulukene)==0:
            lülita_sisse(sinine)
            
        
#Foori töö tsükklis
try:
    while True:
        lülita_sisse(punane_auto)
        if sininee==1:
            lülita_välja(punane_jalakaijad)
            lülita_sisse(roheline_jalakaijad)
            lülita_välja(sinine)
            sininee=0
            roheline=1
        time.sleep(5)
        if roheline == 1:
            lülita_välja(roheline_jalakaijad)
            lülita_sisse(punane_jalakaijad)
            roheline=0
        lülita_välja(punane_auto)
        lülita_sisse(kollane)
        time.sleep(1)
        lülita_välja(kollane)
        lülita_sisse(roheline_auto)
        time.sleep(5)
        lülita_välja(roheline_auto)
        vilgub(kollane)
except:
    GPIO.cleanup()


GPIO.cleanup()