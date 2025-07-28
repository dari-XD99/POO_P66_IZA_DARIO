import tkinter as tk
import threading
import RPi.GPIO as GPIO
import time
from modeloServoM import SensorServo

class InterfazVentana:
    def __init__(self, master):
        self.master = master
        self.master.title("Control Manual de Ventilación")
        self.master.geometry("300x250")

        self.sensor = SensorServo(sensor_pin=4, led_pin=18, servo_pin=17, umbral_temp=28)

        # Configuracion de la interfaz
        self.temp_label = tk.Label(master, text="Temperatura: -- °C", font=("Arial", 12))
        self.hum_label = tk.Label(master, text="Humedad: -- %", font=("Arial", 12))
        self.led_label = tk.Label(master, text="LED: --", font=("Arial", 12), fg="black")

        self.boton_abrir = tk.Button(master, text="Abrir ventana", command=self.abrir)
        self.boton_cerrar = tk.Button(master, text="Cerrar ventana", command=self.cerrar)

        # Disposicion 
        self.temp_label.pack(pady=5)
        self.hum_label.pack(pady=5)
        self.led_label.pack(pady=5)
        self.boton_abrir.pack(pady=5)
        self.boton_cerrar.pack(pady=5)

        # Actualizacion de datos
        self.actualizar_datos()

    def actualizar_datos(self):
        temp, hum = self.sensor.leer()
        if temp is not None and hum is not None:
            self.temp_label.config(text=f"Temperatura: {temp} °C")
            self.hum_label.config(text=f"Humedad: {hum} %")

            if temp > self.sensor.umbral_temp:
                self.led_label.config(text="LED: ENCENDIDO", fg="green")
                GPIO.output(self.sensor.led_pin, GPIO.HIGH)  # Encendido del led
            else:
                self.led_label.config(text="LED: APAGADO", fg="red")
                GPIO.output(self.sensor.led_pin, GPIO.LOW)

        else:
            self.temp_label.config(text="Temperatura: -- °C")
            self.hum_label.config(text="Humedad: -- %")
            self.led_label.config(text="LED: --", fg="black")

        self.master.after(5000, self.actualizar_datos)

    def abrir(self):
        print("Abriendo ventana")
        self.sensor.abrir_ventana()

    def cerrar(self):
        print("Cerrando ventana")
        self.sensor.cerrar_ventana()

    def cerrar_app(self):
        print("Cerrando Interfaz")
        self.sensor.limpiar()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazVentana(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_app)
    root.mainloop()
