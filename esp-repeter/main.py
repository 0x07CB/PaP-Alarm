from machine import Pin, ADC
from utime import sleep
# 
# v1.0
# ESP-Repeater
# Discrtion but it's by me Rick Sanchez
#
def moyenne(lst):
    return sum(lst) / len(lst)

gate=Pin(18,Pin.IN,Pin.PULL_DOWN)
gate_dest=Pin(21,Pin.OUT)#13
predetect_dest=Pin(22,Pin.OUT)
led_predect=Pin(23,Pin.OUT)
builtin_led=Pin(2,Pin.OUT)
TCK=Pin(4,Pin.OUT)
photonic_1=ADC(Pin(35))
photonic_1.atten(ADC.ATTN_11DB)
lst0,pre_detect1,lst1=[],0,[]
while(True):
    lst0.append(photonic_1.read())
    if len(lst0)>3:
        pre_detect1 = moyenne(lst0)
        lst1.append(pre_detect1)
    if len(lst0)>20:
        lst0 = []
        lst1 = []
    
    if pre_detect1 > 80:
        print("PREDECTION")
        predetect_dest.value(1)
        led_predect.value(not led_predect.value())
    else:
        predetect_dest.value(0)
        led_predect.value(0)
    #
    if (gate.value()):
        print("CLOSE")
        gate_dest.value(1)
        builtin_led.value(1)
    if (not gate.value()):
        print("OPEN")
        gate_dest.value(0)
        builtin_led.value(0)
    TCK.value(1)
    sleep(0.5)
    builtin_led.value(0)
    sleep(0.5)
    TCK.value(0)
