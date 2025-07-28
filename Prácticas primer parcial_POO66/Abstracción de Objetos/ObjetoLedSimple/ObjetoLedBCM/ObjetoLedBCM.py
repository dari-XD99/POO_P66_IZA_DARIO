import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        print(f"[INFO] LED configurado en GPIO {self.pin}")

    def encender(self):
        GPIO.output(self.pin, True)

    def apagar(self):
        GPIO.output(self.pin, False)

    def parpadear(self, duracion_encendido=1, duracion_apagado=1, repeticiones=None):
        print(f"[INFO] Iniciando parpadeo del LED en GPIO {self.pin}")
        if repeticiones is None:
            while True:
                self.encender()
                time.sleep(duracion_encendido)
                self.apagar()
                time.sleep(duracion_apagado)
        else:
            for _ in range(repeticiones):
                self.encender()
                time.sleep(duracion_encendido)
                self.apagar()
                time.sleep(duracion_apagado)

led = Led(18)
led.parpadear()