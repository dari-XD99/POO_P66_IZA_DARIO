import tkinter as tk
from tkinter import StringVar, Frame

class VistaDHT11:
    def __init__(self):
        self.controlador = None

        self.ventana = tk.Tk()
        self.ventana.title("Monitor DHT11")
        self.ventana.geometry("420x450")

        self.estado_temp = StringVar()
        self.estado_hum = StringVar()
        self.estado_temp.set("Esperando datos de temperatura...")
        self.estado_hum.set("Esperando datos de humedad...")

        self.banner_temp = Frame(self.ventana, bg="lightgray", padx=10, pady=10)
        self.label_temp = tk.Label(self.banner_temp, textvariable=self.estado_temp, font=("Arial", 12))
        self.label_temp.pack()
        self.banner_temp.pack(pady=5, fill="x")

        self.banner_hum = Frame(self.ventana, bg="lightgray", padx=10, pady=10)
        self.label_hum = tk.Label(self.banner_hum, textvariable=self.estado_hum, font=("Arial", 12))
        self.label_hum.pack()
        self.banner_hum.pack(pady=5, fill="x")

        self.entrada_comando = tk.Entry(self.ventana, width=30)
        self.entrada_comando.pack(pady=10)

        self.boton_enviar = tk.Button(self.ventana, text="Enviar Comando", command=self.enviar_comando)
        self.boton_enviar.pack(pady=5)

        self.boton_modo_boton = tk.Button(self.ventana, text="Control por Botón", command=self.activar_modo_boton)
        self.boton_modo_boton.pack(pady=5)

        self.estado_led_banner = Frame(self.ventana, bg="lightgray", padx=10, pady=10)
        self.label_led = tk.Label(self.estado_led_banner, text="Estado del LED", font=("Arial", 12))
        self.label_led.pack()
        self.estado_led = Frame(self.estado_led_banner, bg="red", width=100, height=30)
        self.estado_led.pack(pady=5)
        self.estado_led_banner.pack(pady=10, fill="x")

        self.datos_sensor = StringVar()
        self.datos_sensor.set("---")
        self.banner_datos = Frame(self.ventana, bg="lightblue", padx=10, pady=10)
        self.label_datos = tk.Label(self.banner_datos, textvariable=self.datos_sensor, font=("Arial", 12))
        self.label_datos.pack()
        self.banner_datos.pack(pady=5, fill="x")

    def set_controlador(self, controlador):
        self.controlador = controlador

    def iniciar(self):
        self.controlador.ejecutar()
        self.ventana.mainloop()

    def mostrar_mensajes(self, mensaje_temp, mensaje_hum):
        self.estado_temp.set(mensaje_temp)
        self.estado_hum.set(mensaje_hum)

    def mostrar_datos(self, temp, hum):
        self.datos_sensor.set(f"Temperatura: {temp}°C  |  Humedad: {hum}%")

    def enviar_comando(self):
        comando = self.entrada_comando.get()
        if self.controlador:
            self.controlador.procesar_comando(comando)
        self.entrada_comando.delete(0, tk.END)

    def activar_modo_boton(self):
        if self.controlador:
            self.controlador.activar_modo_boton()

    def actualizar_estado_led(self, encendido):
        color = "green" if encendido else "red"
        self.estado_led.config(bg=color)