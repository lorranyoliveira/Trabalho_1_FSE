import RPi.GPIO as GPIO


def acende_luz(pino: int):
    print(pino)
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pino,GPIO.OUT)
    
    if GPIO.output(pino) == GPIO.HIGH:
        GPIO.output(pino,GPIO.LOW)
    else:    
        GPIO.output(pino,GPIO.HIGH)