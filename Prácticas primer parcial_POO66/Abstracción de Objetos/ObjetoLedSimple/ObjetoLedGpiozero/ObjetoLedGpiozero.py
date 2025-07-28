from  gpiozero import LED
from time import sleep


class Led:
    def __init__(self, pin):
        self.led = LED(pin)
        print(f"[INFO] LED configurado en pin {pin}")

    def encender(self):
        self.led.on()

    def apagar(self):
        self.led.off()

    def parpadear(self, duracion_encendido=1, duracion_apagado=1, repeticiones=None):
        print(f"[INFO] Iniciando parpadeo del LED en pin {self.led.pin.number}")
        if repeticiones is None:
            while True:
                self.encender()
                sleep(duracion_encendido)
                self.apagar()
                sleep(duracion_apagado)
        else:
            for _ in range(repeticiones):
                self.encender()
                sleep(duracion_encendido)
                self.apagar()
                sleep(duracion_apagado)

led = Led(18)
led.parpadear()