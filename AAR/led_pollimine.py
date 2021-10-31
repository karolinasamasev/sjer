#Import
import RPi.GPIO as GPIO
import time

#Board
GPIO.setmode(GPIO.BOARD)
#to disable warnings
GPIO.setwarnings(False)

punane_led = 3
kollane_led = 5
roheline_led = 7

sinine_led = 8 # Punane jalakäijate jaoks
valge_led = 10 # Roheline jalakäijate jaoks

nuppu_led = 12
nupp = 37

nupp_vajutatud = False


#set gpio... as an output
GPIO.setup(punane_led, GPIO.OUT)
GPIO.setup(kollane_led, GPIO.OUT)
GPIO.setup(roheline_led, GPIO.OUT)
GPIO.setup(sinine_led, GPIO.OUT)
GPIO.setup(valge_led, GPIO.OUT)
GPIO.setup(nuppu_led, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(nupp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Definitsioonid
def lülita_sisse(tulukene):
    GPIO.output(tulukene, GPIO.HIGH)

def lülita_välja(tulukene):
    GPIO.output(tulukene, GPIO.LOW)

def vilgub(tulukene):
    poll(nupp)
    for i in range(2):
        poll(nupp)
        lülita_sisse(tulukene)
        poll(nupp)
        time.sleep(0.4)
        poll(nupp)
        lülita_välja(tulukene)
        poll(nupp)
        time.sleep(0.4)
        poll(nupp)
    lülita_sisse(tulukene)
    poll(nupp)
    time.sleep(0.4)
    poll(nupp)
    lülita_välja(tulukene)
    poll(nupp)
    
def poll(nuppu_kanal):
    print(GPIO.input(nuppu_kanal)) # Inputi kontroll
    global nupp_vajutatud
    if GPIO.input(nuppu_kanal):
        lülita_sisse(nuppu_led)
        nupp_vajutatud = True

#Foori töö tsükklis
try:
    while True:
        poll(nupp)
        lülita_sisse(punane_led)
        poll(nupp)
        if nupp_vajutatud:
            poll(nupp)
            lülita_välja(sinine_led)
            poll(nupp)
            lülita_sisse(valge_led)
            poll(nupp)
            lülita_välja(nuppu_led)
            poll(nupp)
            nupp_vajutatud = False
            poll(nupp)

        time.sleep(5)
        poll(nupp)
        lülita_välja(valge_led)
        poll(nupp)
        lülita_sisse(sinine_led)
        poll(nupp)
        lülita_välja(punane_led)
        poll(nupp)
        lülita_sisse(kollane_led)
        poll(nupp)
        time.sleep(1)
        poll(nupp)
        lülita_välja(kollane_led)
        poll(nupp)
        lülita_sisse(roheline_led)
        poll(nupp)
        time.sleep(5)
        poll(nupp)
        lülita_välja(roheline_led)
        poll(nupp)
        vilgub(kollane_led)
        poll(nupp)

except KeyboardInterrupt:
    print("KeyInter")
except:
    print("Some exception raised")
finally:
    GPIO.cleanup()