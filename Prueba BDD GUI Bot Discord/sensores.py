import dht11
import RPi.GPIO as GPIO
import time
import json
from datetime import datetime

GPIO.setmode(GPIO.BCM)

class SensorError(Exception):
    pass

class SensorBase:
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        raise NotImplementedError("Este sensor no ha implementado 'leer'.")

    def guardar_datos(self, valor):
        datos = {
            "sensor": self.nombre,
            "valor": valor,
            "fecha": datetime.now().isoformat()
        }
        try:
            with open("datos/lecturas.json", "a") as f:
                json.dump(datos, f)
                f.write("\n")
        except Exception as e:
            raise SensorError(f"Error al guardar datos del sensor {self.nombre}: {e}")

class SensorDHT11(SensorBase):
    def __init__(self, pin):
        super().__init__("DHT11")
        self.pin = pin
        self.instancia = dht11.DHT11(pin=self.pin)

    def leer(self):
        resultado = self.instancia.read()
        if not resultado.is_valid():
            raise SensorError("Error leyendo del DHT11")
        temperatura = resultado.temperature
        humedad = resultado.humidity
        self.guardar_datos({"temperatura": temperatura, "humedad": humedad})
        return temperatura, humedad

class SensorHumedadSuelo(SensorBase):
    def __init__(self, pin):
        super().__init__("HumedadSuelo")
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN)

    def leer(self):
        valor = GPIO.input(self.pin)
        humedad = "Alta" if valor == 0 else "Baja"
        self.guardar_datos(humedad)
        return humedad

class SensorUltrasonico(SensorBase):
    def __init__(self, trig, echo):
        super().__init__("Ultrasonico")
        self.trig = trig
        self.echo = echo
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def leer(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            pulso_inicio = time.time()
        while GPIO.input(self.echo) == 1:
            pulso_fin = time.time()

        duracion = pulso_fin - pulso_inicio
        distancia = round((duracion * 34300) / 2, 2)
        self.guardar_datos(distancia)
        return distancia