from modeloDHT11Led import SensorLED

class Controlador:
    def __init__(self):
        
        self.sensor = SensorLED(sensor_pin=4)  # GPIO 4 DHT11

    def obtener_datos(self):
        """Obtiene los datos del sensor (temperatura y humedad)."""
        temp, hum = self.sensor.leer()
        if temp is not None:
            self.sensor.controlar_led(temp)
        return temp, hum
