import RPi.GPIO as gpio
import lirc
import time


if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    redPin = 18
    greenPin = 20
    bluePin = 13
    gpio.setup(redPin, gpio.OUT)
    gpio.setup(greenPin, gpio.OUT)
    gpio.setup(bluePin, gpio.OUT)
    with lirc.LircdConnection("control.py") as lc:
        while True:
            cmd = lc.readline()
            if cmd == 'echo "KEY_1"':
                gpio.output(redPin, gpio.HIGH)
                time.sleep(0.5)
                gpio.output(redPin, gpio.LOW)

            elif cmd == 'echo "KEY_2"':
                gpio.output(greenPin, gpio.HIGH)
                time.sleep(0.5)
                gpio.output(greenPin, gpio.LOW)

            elif cmd == 'echo "KEY_3"':
                gpio.output(bluePin, gpio.HIGH)
                time.sleep(0.5)
                gpio.output(bluePin, gpio.LOW)
