import tkinter as tk
from controladorS import Controlador

class InterfazSistema:
    def __init__(self, master):
        self.master = master
        self.master.title("Monitor Ambiental Raspberry Pi")
        self.master.geometry("350x300")
        self.controlador = Controlador()

        # Configuracion
        self.temp_label = tk.Label(master, text="Temperatura: -- °C", font=("Arial", 12))
        self.hum_label = tk.Label(master, text="Humedad: -- %", font=("Arial", 12))
        self.suelo_label = tk.Label(master, text="Suelo: --", font=("Arial", 12))
        self.led_label = tk.Label(master, text="LED: --", font=("Arial", 12))

        # Botones
        self.actualizar_btn = tk.Button(master, text="Actualizar datos", command=self.actualizar_datos)
        self.abrir_btn = tk.Button(master, text="Abrir ventana", command=self.abrir_ventana)
        self.cerrar_btn = tk.Button(master, text="Cerrar ventana", command=self.cerrar_ventana)
        self.salir_btn = tk.Button(master, text="Salir", command=self.salir)

        
        self.temp_label.pack(pady=5)
        self.hum_label.pack(pady=5)
        self.suelo_label.pack(pady=5)
        self.led_label.pack(pady=5)
        self.actualizar_btn.pack(pady=5)
        self.abrir_btn.pack(pady=5)
        self.cerrar_btn.pack(pady=5)
        self.salir_btn.pack(pady=5)

        # Actualización de los datos
        self.actualizar_datos()

    def actualizar_datos(self):
        temp, hum = self.controlador.obtener_datos_ambiente()
        suelo_seco = self.controlador.obtener_estado_suelo()

        if temp is not None:
            self.temp_label.config(text=f"Temperatura: {temp} °C")
            self.hum_label.config(text=f"Humedad: {hum} %")
            if temp > self.controlador.sistema.umbral_temp:
                self.led_label.config(text="LED: ENCENDIDO", fg="green")
            else:
                self.led_label.config(text="LED: APAGADO", fg="red")
        else:
            self.temp_label.config(text="Temperatura: -- °C")
            self.hum_label.config(text="Humedad: -- %")
            self.led_label.config(text="LED: --", fg="black")

        estado_suelo = "SECO" if suelo_seco else "HÚMEDO"
        self.suelo_label.config(text=f"Suelo: {estado_suelo}")

    def abrir_ventana(self):
        self.controlador.abrir_ventana()

    def cerrar_ventana(self):
        self.controlador.cerrar_ventana()

    def salir(self):
        self.controlador.limpiar()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSistema(root)
    root.protocol("WM_DELETE_WINDOW", app.salir)
    root.mainloop()