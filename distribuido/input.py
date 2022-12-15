import RPi.GPIO as GPIO


def muda_estado_output(pino: int):
    print(pino)
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pino,GPIO.OUT)
    
    if GPIO.output(pino) == GPIO.HIGH:
        GPIO.output(pino,GPIO.LOW)
    else:    
        GPIO.output(pino,GPIO.HIGH)