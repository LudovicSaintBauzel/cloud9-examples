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

LEDs=3
BUTTON="P8_19"
BUZZER="P8_13"
GPIO.setup(BUTTON,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)
for i in range(LEDs):
    j=15+i
    GPIO.setup("P8_%d" % j, GPIO.OUT)

while True:
    for i in range(LEDs):
        j=15+i
        GPIO.output("P8_%d" % j, GPIO.HIGH)
        time.sleep(0.25)
    for i in range(LEDs):
        j=15+i
        GPIO.output("P8_%d" % j, GPIO.LOW)
        time.sleep(0.25)
    if(GPIO.input(BUTTON)):
        GPIO.output(BUZZER,GPIO.HIGH)
    else:
        GPIO.output(BUZZER,GPIO.LOW)

            