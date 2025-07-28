import RPi.GPIO as GPIO

class LedModel:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, 0)  

    def turn_on(self):
        GPIO.output(self.pin, 1)

    def turn_off(self):
        GPIO.output(self.pin, 0)
