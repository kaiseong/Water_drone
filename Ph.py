from itertools import count
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.14)

def Ph(pin_num):
    GPIO.setup(pin_num,GPIO.OUT)
    GPIO.output(pin_num,GPIO.LOW)
    time.sleep(0.1)
    
    GPIO.setup(pin_num,GPIO.IN)
    
    while (GPIO.input(pin_num)==GPIO.LOW):
        count+=1
        
    return count

try:
    while True:
        print(Ph(pin_num))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
