from gpiozero import LED
from time import sleep

sekvens = 1

NSgreen = LED(26)
NSyellow = LED(19)
NSred = LED(13)

VEgreen = LED(17)
VEyellow = LED(27)
VEred = LED(22)

def state0():
    NSgreen.off()
    NSyellow.off()
    NSred.on()

    VEgreen.off()
    VEyellow.off()
    VEred.on()
    sleep(1)
    ######## NORTH SOUTH GREEN #######
    if sekvens == 1:
        return(state1)
    elif sekvens == 2:
        return(state2)


def state1():
    ########## NORTH SOUTH  ############
    NSgreen.off()
    NSyellow.on()
    NSred.on()

    sleep(2)

    NSgreen.on()
    NSyellow.off()
    NSred.off()

    sleep(6)

    NSgreen.off()
    NSyellow.on()
    NSred.off()
    global sekvens
    sekvens = 2
    sleep(1)
    return(state0)

def state2():
    ########## VEST EAST  ##############
    VEgreen.off()
    VEyellow.on()
    VEred.on()

    sleep(2)

    VEgreen.on()
    VEyellow.off()
    VEred.off()

    sleep(6)

    VEgreen.off()
    VEyellow.on()
    VEred.off()

    global sekvens
    sekvens = 1
    sleep(1)
    return(state0)


state = state0
while state: state=state()