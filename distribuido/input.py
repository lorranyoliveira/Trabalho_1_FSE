import RPi.GPIO as GPIO
import time

def muda_estado_input(pino: int, pino2: int):
    print(pino)
    print(pino2)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    GPIO.setup(pino,GPIO.IN)
    GPIO.setup(pino2,GPIO.OUT)
    
    
    if GPIO.input(pino)==1:
        GPIO.output(pino2,GPIO.HIGH)
        return True
    else:
        GPIO.output(pino2,GPIO.LOW)
        return False