import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    gpio.setmode(gpio.BCM)
    buzzerPin = 13
    gpio.setup(buzzerPin, gpio.OUT)
    f = [440, 494, 554, 587, 659, 740, 831, 880]
    
    for i in range(len(f)):
        pwm = gpio.PWM(buzzerPin, f[i])
        pwm.start(0)
        pwm.ChangeDutyCycle(50)
        time.sleep(1)
        pwm.stop()
        
    gpio.cleanup()
    
    
