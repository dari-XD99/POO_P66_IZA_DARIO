import RPi.GPIO as GPIO
import dht11
import time

class SensorServo:
    def __init__(self, sensor_pin=4, led_pin=18, servo_pin=17, umbral_temp=28):
        self.sensor_pin = sensor_pin
        self.led_pin = led_pin
        self.servo_pin = servo_pin
        self.umbral_temp = umbral_temp

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.servo_pin, GPIO.OUT)

        self.servo = GPIO.PWM(self.servo_pin, 50)  # 50 Hz servo motor
        self.servo.start(0)

        self.sensor = dht11.DHT11(pin=self.sensor_pin)

    def leer(self):
        for _ in range(3):
            result = self.sensor.read()
            if result.is_valid():
                return round(result.temperature, 1), round(result.humidity, 1)
            time.sleep(0.5)
        return None, None

    def controlar_actuadores(self, temperatura):
        print(f"Temperatura actual: {temperatura}°C")
        if temperatura > self.umbral_temp:
            print("Temperatura alta: Abriendo ventana y encendiendo LED.")
            GPIO.output(self.led_pin, GPIO.HIGH)
            self.abrir_ventana()
        else:
            print("Temperatura normal: Cerrando ventana y apagando LED.")
            GPIO.output(self.led_pin, GPIO.LOW)
            self.cerrar_ventana()

    def abrir_ventana(self):
        self.servo.ChangeDutyCycle(12.5)  # 180°
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)

    def cerrar_ventana(self):
        self.servo.ChangeDutyCycle(2.5)  # 0°
        time.sleep(0.5)
        self.servo.ChangeDutyCycle(0)

    def limpiar(self):
        self.servo.stop()
        GPIO.cleanup()