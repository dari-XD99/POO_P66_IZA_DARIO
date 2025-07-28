from modeloServoM import SensorServo

class Controlador:
    def __init__(self):
        self.sensor = SensorServo(sensor_pin=4, led_pin=18, servo_pin=17, umbral_temp=28)

    def obtener_datos(self):
        temp, hum = self.sensor.leer()
        if temp is not None:
            self.sensor.controlar_actuadores(temp)
        return temp, hum

    def limpiar(self):
        self.sensor.limpiar()
