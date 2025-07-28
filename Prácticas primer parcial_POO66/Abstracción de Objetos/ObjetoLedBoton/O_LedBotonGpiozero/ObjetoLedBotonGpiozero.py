from gpiozero import LED, Button
from signal import pause

class LedControl:
    def __init__(self, pin_led, pin_boton):
        self.led = LED(pin_led)
        self.boton = Button(pin_boton, pull_up=True)
        print(f"[INFO] LED en GPIO {pin_led}, botón en GPIO {pin_boton}")
        self.boton.when_pressed = self.led.on
        self.boton.when_released = self.led.off

    def iniciar(self):
        pause() 


LED_GPIO = 18
BOTON_GPIO = 25


control = LedControl(LED_GPIO, BOTON_GPIO)
control.iniciar()