#!/usr/bin/env python3
# ////////////////////////////////////////
# //	seqLED.py
# //      Blinks the USR LEDs in sequence.
# //	Wiring:
# //	Setup:	
# //	See:	
# ////////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time
import os
LEDs=3
BUTTON="P8_19"
BUZZER="P8_13"
RED="P8_16"
GREEN="P8_17"
BLUE="P8_15"
GPIO.setup(BUTTON,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
for i in range(LEDs):
    j=15+i
    GPIO.setup("P8_%d" % j, GPIO.OUT)
def ledBlink(pin,delay=0.25,nb=3):
    for ii in range(nb):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(delay)
        
        

def checkESSID(essid_str):
    res_str=os.popen("iwconfig wlan0").read()
    return essid_str in res_str

#--------------------Warming UP Process
mystr = "No Wifi Yet"
GPIO.output(BLUE,GPIO.HIGH)
while True:
    
    if(GPIO.input(BUTTON) or checkESSID("Poupsland")):
        mystr=os.popen("/var/lib/cloud9/buttonbox-startup/wifirestart.sh").read()
        if "Enabled wifi" in mystr:
            GPIO.output(BLUE, GPIO.LOW)
            ledBlink(GREEN,0.25,3)
            # GPIO.output(GREEN, GPIO.HIGH)
            # time.sleep(0.5)
            # GPIO.output(GREEN, GPIO.LOW)
            # time.sleep(0.5)
            # GPIO.output(GREEN, GPIO.HIGH)
            # time.sleep(0.5)
            # GPIO.output(GREEN, GPIO.LOW)
            # time.sleep(0.5)
            # GPIO.output(GREEN, GPIO.HIGH)
            # time.sleep(0.5)
            # GPIO.output(GREEN, GPIO.LOW)
            # time.sleep(0.5)
            break
        else:
            GPIO.output(BLUE, GPIO.LOW)
            ledBlink(RED,0.25,2)
        GPIO.output(BLUE,GPIO.HIGH)
        time.sleep(0.20)

#-------------------Main loop
while True:
    for i in range(LEDs):
        j=15+i
        GPIO.output("P8_%d" % j, GPIO.HIGH)
        time.sleep(0.1)
    for i in range(LEDs):
        j=15+i
        GPIO.output("P8_%d" % j, GPIO.LOW)
        time.sleep(0.1)
    if(GPIO.input(BUTTON)):
        GPIO.output(BUZZER,GPIO.HIGH)
    else:
        GPIO.output(BUZZER,GPIO.LOW)

            
