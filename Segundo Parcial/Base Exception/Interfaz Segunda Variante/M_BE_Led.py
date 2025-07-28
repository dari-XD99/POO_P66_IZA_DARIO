import RPi.GPIO as GPIO

class ModeloLed:
    def __init__(self):
        self.LED_PIN = 18
        self.BOTON_PIN = 25
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_PIN, GPIO.OUT)
        GPIO.setup(self.BOTON_PIN, GPIO.IN)
        self.led_estado = False

    def leer_boton(self):
        return GPIO.input(self.BOTON_PIN) == 0

    def encender_led(self):
        GPIO.output(self.LED_PIN, True)
        self.led_estado = True

    def apagar_led(self):
        GPIO.output(self.LED_PIN, False)
        self.led_estado = False

    def obtener_estado_led(self):
        return self.led_estado
