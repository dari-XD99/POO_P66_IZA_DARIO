import RPi.GPIO as GPIO
import dht11
import time

class SensorLED:
    def __init__(self, sensor_pin=4, led_pin=18, umbral_temp=25):
        self.sensor_pin = sensor_pin
        self.led_pin = led_pin
        self.umbral_temp = umbral_temp

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)

        self.sensor = dht11.DHT11(pin=self.sensor_pin)

    def leer(self):
        """Lee los datos del sensor DHT11 (temperatura y humedad)"""
        for _ in range(3):
            result = self.sensor.read()
            if result.is_valid():
                return round(result.temperature, 1), round(result.humidity, 1)
            time.sleep(0.5)
        return None, None

    def controlar_led(self, temperatura):
        print(f"Temperatura leída: {temperatura}°C")
        if temperatura > self.umbral_temp:
            print("LED Encendido")
            GPIO.output(self.led_pin, GPIO.HIGH)
        else:
            print("LED Apagado")
            GPIO.output(self.led_pin, GPIO.LOW)

    def limpiar(self):
        """Limpia los recursos de GPIO"""
        GPIO.cleanup()
