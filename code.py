import time
import display
import buttons
import lora
import led
import motor
import msg

sel = 0


def alert(txt):
    led.on()
    motor.on()
    display.shw_msg(txt)
    time.sleep(2)
    motor.off()
    time.sleep(3)
    led.off()


def run():
    display.init()
    lora.init()
    display.shw_menu(msg.codes, sel)

    while True:
        if buttons.up_prsd():
            move(-1)
        elif buttons.dw_prsd():
            move(1)
        elif buttons.snd_prsd():
            cd = msg.codes[sel]
            lora.send(cd)
            time.sleep(0.3)

        cd = lora.recv()
        if cd is not None:
            txt = msg.lookup(cd)
            alert(txt)
            display.shw_menu(msg.codes, sel)

        time.sleep(0.1)


def move(step):
    global sel
    sel = (sel + step) % len(msg.codes)
    display.shw_menu(msg.codes, sel)