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

sinine_led = 8 #punane jalakäijate jaoks

valge_led = 10 #roheline jalakäijate jaoks

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
GPIO.setup(nupp, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #tehtud tarkvara poolt

#definitsioonid
def lülita_sisse(tuli):
    GPIO.output(tuli, GPIO.HIGH)

def lülita_välja(tuli):
    GPIO.output(tuli, GPIO.LOW)

def vilgub(tuli):
    
    for i in range(2):
        lülita_sisse(tuli)
        time.sleep(0.4)
        lülita_välja(tuli)
        time.sleep(0.4)
    lülita_sisse(tuli)
    time.sleep(0.4)
    lülita_välja(tuli)
    
    
def callback(nuppu_kanal): #lülitab sisse ledi
    global nupp_vajutatud
    nupp_vajutatud = True
    lülita_sisse(nuppu_led)

GPIO.add_event_detect(nupp, GPIO.RISING, callback) #lisab kogu protsessi "tagaplaanile"

#tsükkel foori töö jaoks
try:
    while True:
        lülita_sisse(punane_led)
        if nupp_vajutatud:
            lülita_välja(sinine_led)
            lülita_sisse(valge_led)
            lülita_välja(nuppu_led)
            nupp_vajutatud = False

        time.sleep(5)
        lülita_välja(valge_led)
        lülita_sisse(sinine_led)
        lülita_välja(punane_led)
        lülita_sisse(kollane_led)
        time.sleep(1)
        lülita_välja(kollane_led)
        lülita_sisse(roheline_led)
        time.sleep(5)
        lülita_välja(roheline_led)
        vilgub(kollane_led)

except KeyboardInterrupt:
    print("KeyInter")
except:
    print("Some exception raised")
finally:
    GPIO.cleanup()