import RPi.GPIO as GPIO
import time

def muda_estado_output(pino: int):
    print(pino)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pino,GPIO.OUT)
    
    if GPIO.input(pino)==0:
        GPIO.output(pino,GPIO.HIGH)
        return True
    else:
        GPIO.output(pino,GPIO.LOW)
        return False