from machine import Pin, PWM
from time import sleep

led = PWM(Pin(25))


def ledon(brightness=10000):
    led.duty_u16(brightness)


while True:
    for i in range(0, 10000, 1000):
        ledon(i)
        sleep(0.1)

    for i in range(10000, 0, -1000):
        ledon(i)
        sleep(0.1)
