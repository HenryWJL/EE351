import RPi.GPIO as gpio
import time

if __name__ == "__main__":
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    trig_pin = 17
    echo_pin = 18
    gpio.setup(trig_pin, gpio.OUT)
    gpio.setup(echo_pin, gpio.IN)

    while(True):
        gpio.output(trig_pin, gpio.LOW)
        gpio.output(trig_pin, gpio.HIGH)
        time.sleep(0.001)
        gpio.output(trig_pin, gpio.LOW)

        while(gpio.input(echo_pin) == gpio.LOW):
            pass

        t1 = time.time()
        while(gpio.input(echo_pin) == gpio.HIGH):
            pass

        t2 = time.time()
        d = (t2 - t1) * 340 / 2
        print("distance: %f m" % d)
        time.sleep(1)
