from machine import Pin, SPI
import pins

spi = SPI(1, baudrate=2000000, sck=Pin(pins.spi_sck), mosi=Pin(pins.spi_mosi), miso=Pin(pins.spi_miso))
cs = Pin(pins.lora_cs, Pin.OUT, value=1)
rst = Pin(pins.lora_rst, Pin.OUT)
d0 = Pin(pins.lora_d0, Pin.IN)


def init():
    rst.value(0)
    rst.value(1)
    


def send(cd):
    cs.value(0)
    
    cs.value(1)
    print("lora tx:", cd)


def recv():
    if d0.value() == 1:
        
        return None
    return None
