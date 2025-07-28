import RPi.GPIO as GPIO
import dht11
import time


class DHT11Sensor:
    def __init__(self, gpio_pin):
        self.gpio_pin = gpio_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.sensor = dht11.DHT11(pin=self.gpio_pin)

    def leer(self):
        for _ in range(3):  
            result = self.sensor.read()
            if result.is_valid():
                return round(result.temperature, 1), round(result.humidity, 1)
            time.sleep(0.5)
        return None, None


def mostrar_datos(temperatura, humedad):
    if temperatura is not None and humedad is not None:
        print(f"Temperatura: {temperatura} C  |  Humedad: {humedad} %")
    else:
        print("Error al leer el sensor DHT11.")


def main():
    sensor = DHT11Sensor(gpio_pin=4)  # DHT11 conectado al GPIO 4
    led_pin = 18                      
    GPIO.setup(led_pin, GPIO.OUT)

    try:
        while True:
            temp, hum = sensor.leer()
            mostrar_datos(temp, hum)

            # Encender el LED si la temperatura supera los 25°C
            if temp is not None and temp > 25:
                GPIO.output(led_pin, GPIO.HIGH)
            else:
                GPIO.output(led_pin, GPIO.LOW)

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()
