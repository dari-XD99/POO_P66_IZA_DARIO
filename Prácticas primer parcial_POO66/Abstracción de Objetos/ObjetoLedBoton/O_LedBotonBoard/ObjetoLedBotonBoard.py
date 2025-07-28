import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin_led, pin_boton):
        self.pin_led = pin_led
        self.pin_boton = pin_boton

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.pin_led, GPIO.OUT)
        GPIO.setup(self.pin_boton, GPIO.IN)

        print(f"[INFO] LED en GPIO {self.pin_led}, botón en GPIO {self.pin_boton}")

    def controlar_con_boton(self):
        try:
            while True:
                if GPIO.input(self.pin_boton) == GPIO.LOW:
                    GPIO.output(self.pin_led, GPIO.HIGH)
                else:
                    GPIO.output(self.pin_led, GPIO.LOW)
                time.sleep(0.01)
        except KeyboardInterrupt:
            GPIO.cleanup()


LED_GPIO = 12
BOTON_GPIO = 22


led_control = Led(LED_GPIO, BOTON_GPIO)
led_control.controlar_con_boton()