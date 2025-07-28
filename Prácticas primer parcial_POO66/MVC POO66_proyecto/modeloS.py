import RPi.GPIO as GPIO
import dht11
import time

class SistemaSensorial:
    def __init__(self, sensor_pin=4, led_pin=18, servo_pin=17, soil_pin=27, umbral_temp=28):
        self.sensor_pin = sensor_pin
        self.led_pin = led_pin
        self.servo_pin = servo_pin
        self.soil_pin = soil_pin
        self.umbral_temp = umbral_temp

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        GPIO.setup(self.soil_pin, GPIO.IN)

        self.servo = GPIO.PWM(self.servo_pin, 50)
        self.servo.start(0)

        self.sensor = dht11.DHT11(pin=self.sensor_pin)

    def leer_temperatura_humedad(self):
        for _ in range(3):
            result = self.sensor.read()
            if result.is_valid():
                return round(result.temperature, 1), round(result.humidity, 1)
            time.sleep(0.5)
        return None, None

    def leer_suelo(self):
        return GPIO.input(self.soil_pin) == GPIO.HIGH  # True = seco, False = húmedo

    def abrir_ventana(self):
        self.servo.ChangeDutyCycle(12.5)
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)

    def cerrar_ventana(self):
        self.servo.ChangeDutyCycle(2.5)
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)

    def encender_led(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def apagar_led(self):
        GPIO.output(self.led_pin, GPIO.LOW)

    def limpiar(self):
        self.servo.stop()
        GPIO.cleanup()
