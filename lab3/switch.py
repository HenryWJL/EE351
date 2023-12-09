import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    ledRedPin = 13
    ledGreenPin = 19
    switchPin = 17
    gpio.setup(ledRedPin, gpio.OUT)
    gpio.setup(ledGreenPin, gpio.OUT)
    gpio.setup(switchPin, gpio.IN)

    while True:
        cmd = gpio.input(switchPin)
        if(cmd == gpio.LOW):
            gpio.output(ledGreenPin, gpio.LOW)
            gpio.output(ledRedPin, gpio.HIGH)
        else:
            gpio.output(ledGreenPin, gpio.HIGH)
            gpio.output(ledRedPin, gpio.LOW)
