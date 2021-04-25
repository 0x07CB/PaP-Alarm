from gpiozero import Button,LED,DigitalInputDevice
from time import sleep
import os
from multiprocessing import Process
porte = DigitalInputDevice("GPIO13")#4,pull_up=True)
led1 = LED("GPIO21")
led_work = LED("GPIO26")
predect=DigitalInputDevice("GPIO4")

def blinkalert():
    while True:
        led1.on()
        sleep(0.255)
        led1.off()
        sleep(0.255)


p = Process(target=blinkalert)

while True:
    led_work.on()
    sleep(0.5)
    if predect.value:
        print("PRESENCE OR ANOMALY DETECTED !")
    if not porte.value:
        led1.off()
        if not p.is_alive(): p.start()
        os.system('espeak -a 200 -ven-us -s120 "Alert door are opened!"')
        print("Pressed")
    else:
        if p.is_alive(): 
            p.kill()
            p = Process(target=blinkalert)
        led1.on()
        print("Released")
    led_work.off()
    sleep(0.5)

