import RPi.GPIO as GPIO
import dht11
import time

class ModeloDHT11:
    def __init__(self):
        self.GPIO_PIN_SENSOR = 22
        self.GPIO_PIN_LED = 18
        self.GPIO_PIN_BOTON = 25

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.GPIO_PIN_LED, GPIO.OUT)
        GPIO.setup(self.GPIO_PIN_BOTON, GPIO.IN)

        self.sensor = dht11.DHT11(pin=self.GPIO_PIN_SENSOR)
        self.control_por_boton = False
        self.led_encendido = False

    def leer_datos(self):
        resultado = self.sensor.read()
        if resultado.is_valid():
            return resultado.temperature, resultado.humidity
        else:
            return None, None

    def encender_led(self):
        GPIO.output(self.GPIO_PIN_LED, True)
        self.led_encendido = True

    def apagar_led(self):
        GPIO.output(self.GPIO_PIN_LED, False)
        self.led_encendido = False

    def leer_boton(self):
        return GPIO.input(self.GPIO_PIN_BOTON)

    def activar_control_por_boton(self):
        self.control_por_boton = True

    def desactivar_control_por_boton(self):
        self.control_por_boton = False

    def esta_en_modo_boton(self):
        return self.control_por_boton

    def esta_led_encendido(self):
        return self.led_encendido