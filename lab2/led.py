import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    ledRedPin = 13
    gpio.setup(ledRedPin, gpio.OUT)
    for i in range(20):
        gpio.output(ledRedPin, gpio.HIGH)
        time.sleep(0.1)
        gpio.output(ledRedPin, gpio.LOW)
        time.sleep(0.1)
    gpio.cleanup()
