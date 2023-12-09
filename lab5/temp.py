import RPi.GPIO as gpio
import smbus
import time
import math


if __name__ == "__main__":
    # Constants
    T0 = 298.15
    R0 = 10000
    B = 3950
    # Setup
    pin = 17
    address = 0x48
    gpio.setmode(gpio.BCM)
    gpio.setup(pin, gpio.IN)
    bus = smbus.SMBus(1)
    while True:
        analogVal = bus.read_byte_data(address, 0)
        digitalVal = gpio.input(pin)
        Vr = 5 * float(analogVal) / 255
        Rt = 10000 * Vr / (5 - Vr)
        T = 1 / (1 / T0 + math.log(Rt / R0) / B)
        T = T - 273.15
        print("Temperature: %f" % T)
        time.sleep(1)
