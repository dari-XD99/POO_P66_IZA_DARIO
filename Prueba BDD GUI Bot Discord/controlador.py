from modelo.sensores import SensorDHT11, SensorHumedadSuelo, SensorUltrasonico, SensorError

class ControladorSensores:
    def __init__(self):
        self.dht = SensorDHT11(pin=4)
        self.suelo = SensorHumedadSuelo(pin=17)
        self.ultra = SensorUltrasonico(trig=23, echo=24)

    def obtener_temperatura(self):
        try:
            temp, _ = self.dht.leer()
            return f"Temperatura: {temp} °C"
        except SensorError as e:
            return str(e)

    def obtener_humedad(self):
        try:
            _, hum = self.dht.leer()
            return f"Humedad ambiental: {hum} %"
        except SensorError as e:
            return str(e)

    def obtener_humedad_suelo(self):
        try:
            humedad = self.suelo.leer()
            return f"Humedad del suelo: {humedad}"
        except SensorError as e:
            return str(e)

    def obtener_distancia(self):
        try:
            distancia = self.ultra.leer()
            return f"Distancia detectada: {distancia} cm"
        except SensorError as e:
            return str(e)