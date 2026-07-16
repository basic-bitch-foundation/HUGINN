from machine import Pin, SPI
import pins


spi = SPI(1, baudrate=4000000, sck=Pin(pins.spi_sck), mosi=Pin(pins.spi_mosi), miso=Pin(pins.spi_miso))
cs = Pin(pins.ep_cs, Pin.OUT, value=1)
dc = Pin(pins.ep_dc, Pin.OUT)

rst = Pin(pins.ep_rst, Pin.OUT)

bsy = Pin(pins.ep_bsy, Pin.IN)



def init():
    rst.value(0)

    rst.value(1)

    


def clr():
    cs.value(1)
    
    dc.value(1)
    


def shw_menu(codes, sel):
    clr()
    for i, cd in enumerate(codes):
        mark = "* " if i == sel else "  "
        print(mark + str(cd))
    refresh()


def shw_msg(txt):
    clr()
    print("Incoming Message")
    print(txt)
    refresh()


def refresh():
    cs.value(0)
    
    cs.value(1)
    