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
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Definitsioonid
def lülita_sisse(tulukene):
    GPIO.output(tulukene, GPIO.HIGH)

def lülita_välja(tulukene):
    GPIO.output(tulukene, GPIO.LOW)

def vilgub(tulukene):
    for i in range(3):
        lülita_sisse(tulukene)
        ajavott(1/3)
        lülita_välja(tulukene)
        ajavott(1/3)

sininee=0
roheline=0
def ajavott(ootamine):
    aeg=time.time()
    muutuja=0
    global sininee
    while True:
        muutuja=time.time()
        if GPIO.input(nupp)==GPIO.HIGH:
            lülita_sisse(sinine)
            sininee=1
        if muutuja>=aeg+ootamine:
            break

#Muutujad
punane_jalakaijad=37
punane_auto=18
kollane=22
roheline_auto=11
roheline_jalakaijad=31
sinine=13
nupp=16


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
        ajavott(5)
        if roheline == 1:
            lülita_välja(roheline_jalakaijad)
            lülita_sisse(punane_jalakaijad)
            roheline=0
        lülita_välja(punane_auto)
        lülita_sisse(kollane)
        ajavott(1)
        lülita_välja(kollane)
        lülita_sisse(roheline_auto)
        ajavott(5)
        lülita_välja(roheline_auto)
        vilgub(kollane)
except:
    GPIO.cleanup()