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
    cnt = 0

    while True:
        cmd = gpio.input(switchPin)
        if(cmd == gpio.LOW):
            if(cnt % 4 == 0):
                gpio.output(ledGreenPin, gpio.LOW)
                gpio.output(ledRedPin, gpio.HIGH)
                time.sleep(1)
                cnt += 1
            elif(cnt % 4 == 1):
                for i in range(5):
                    gpio.output(ledRedPin, gpio.HIGH)
                    time.sleep(0.1)
                    gpio.output(ledRedPin, gpio.LOW)
                    time.sleep(0.1)
                cnt += 1
            elif(cnt % 4 == 2):
                gpio.output(ledGreenPin, gpio.HIGH)
                gpio.output(ledRedPin, gpio.LOW)
                time.sleep(1)
                cnt += 1
            else:
                for i in range(5):
                    gpio.output(ledGreenPin, gpio.HIGH)
                    time.sleep(0.1)
                    gpio.output(ledGreenPin, gpio.LOW)
                    time.sleep(0.1)
                cnt += 1
            gpio.output(ledGreenPin, gpio.LOW)
            gpio.output(ledRedPin, gpio.LOW)

    gpio.cleanup()
	
