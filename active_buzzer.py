import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    buzzerPin = 17
    gpio.setup(buzzerPin, gpio.OUT)
    for i in range(20):
        gpio.output(buzzerPin, gpio.HIGH)
        time.sleep(0.1)
        gpio.output(buzzerPin, gpio.LOW)
        time.sleep(0.1)
    gpio.cleanup()
