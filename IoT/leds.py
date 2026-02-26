import machine
from machine import Pin 
import time


red_led = Pin(28, Pin.OUT)
while True :

    red_led.on()  
    time.sleep(1) # Wait for USB to become ready
    red_led.off()
    time.sleep(1)
    yellow_led = Pin(27, Pin.OUT)
    yellow_led.off()  
    time.sleep(1) # Wait for USB to become ready
    yellow_led.on()
    time.sleep(1)
    print("the great puhseidon king")