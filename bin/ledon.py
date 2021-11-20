from machine import Pin, PWM

led = PWM(Pin(25))
led.duty_u16(65535)
