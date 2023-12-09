import RPi.GPIO as gpio
import smbus
import time
import math


if __name__ == "__main__":
    # Setup
    led_pin = 17
    ps2_pin = 18
    address = 0x48
    gpio.setmode(gpio.BCM)
    gpio.setup(led_pin, gpio.OUT)
    gpio.setup(ps2_pin, gpio.IN)
    bus = smbus.SMBus(1)
    while True:
        x_analogVal = bus.read_byte_data(address, 0)
        y_analogVal = bus.read_byte_data(address, 1)
        digitalVal = bus.read_byte_data(address, 2)
        print("x_analog_value: %d" % x_analogVal)
        print("y_analog_value: %d" % y_analogVal)
        print("digital_value: %d" % digitalVal)
        if (digitalVal > 5):
            bus.write_byte_data(address, 0x40, x_analogVal)
        else:
            gpio.output(led_pin, gpio.HIGH)
            time.sleep(1)
            gpio.output(led_pin, gpio.LOW)
        time.sleep(1)
	
	
