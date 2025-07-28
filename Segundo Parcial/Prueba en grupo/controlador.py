import RPi.GPIO as GPIO
import dht11
from modelo import BaseDatos

class ControladorSensor:
    def __init__(self, pin_dht=4):
        self.db = BaseDatos()
        self.pin = pin_dht
        GPIO.setmode(GPIO.BCM)
        self.sensor = dht11.DHT11(pin=self.pin)

    def leer_datos(self):
        try:
            resultado = self.sensor.read()

            if not resultado.is_valid():
                raise ValueError("Lectura inválida del sensor DHT11")

            temp = resultado.temperature
            hum = resultado.humidity

            estado = "Normal"
            if temp > 30 or hum < 30:
                estado = "Crítico"

            self.db.insertar_lectura(id_sensor=1, temperatura=temp, humedad=hum, estado=estado)
            return (temp, hum, estado)

        except ValueError as ve:
            print(f"[ERROR] {ve}")
            return None

        except Exception as e:
            print(f"[EXCEPCIÓN INESPERADA] {e}")
            return None
