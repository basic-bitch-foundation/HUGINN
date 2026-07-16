from machine import Pin
import pins

gt = Pin(pins.mtr_gt, Pin.OUT)


def on():
    gt.value(1)


def off():
    gt.value(0)
    
    