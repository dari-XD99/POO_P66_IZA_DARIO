import tkinter as tk
from tkinter import StringVar, messagebox

class VistaLedGUI:
    def __init__(self):
        self.controlador = None

        self.ventana = tk.Tk()
        self.ventana.title("Control de LED")
        self.ventana.geometry("300x200")
        self.ventana.resizable(False, False)

        self.estado_led = StringVar()
        self.estado_led.set("LED apagado")

        self.label_estado = tk.Label(self.ventana, textvariable=self.estado_led, font=("Arial", 14))
        self.label_estado.pack(pady=10)

        self.label_modo = tk.Label(self.ventana, text="Modo actual: COMANDO", font=("Arial", 12))
        self.label_modo.pack(pady=5)

        self.entry_comando = tk.Entry(self.ventana, width=25)
        self.entry_comando.pack(pady=5)

        self.btn_enviar = tk.Button(self.ventana, text="Enviar Comando", command=self.enviar_comando)
        self.btn_enviar.pack(pady=5)

        self.btn_modo_boton = tk.Button(self.ventana, text="Control por Botón")
        self.btn_modo_boton.pack(pady=5)

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.btn_modo_boton.config(command=self.controlador.activar_modo_boton)

    def iniciar(self):
        self.controlador.ejecutar()
        self.ventana.mainloop()

    def actualizar_estado_led(self, encendido):
        self.estado_led.set("LED encendido" if encendido else "LED apagado")

    def actualizar_modo(self, modo):
        self.label_modo.config(text=f"Modo actual: {modo}")

    def mostrar_error_comando(self):
        messagebox.showwarning("Error", "Comando Invalido")

    def enviar_comando(self):
        comando = self.entry_comando.get()
        if self.controlador:
            self.controlador.procesar_comando(comando)
        self.entry_comando.delete(0, tk.END)
