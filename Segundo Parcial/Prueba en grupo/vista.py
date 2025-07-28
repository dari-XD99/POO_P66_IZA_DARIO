import tkinter as tk
from tkinter import ttk, messagebox
from controlador import ControladorSensor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class VistaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitoreo Ambiental IoT")
        self.root.geometry("700x500")

        self.controlador = ControladorSensor()

        # Crear pestañas con ttk.Frame
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.tab_lectura = ttk.Frame(self.notebook)
        self.tab_graficas = ttk.Frame(self.notebook)
        self.tab_consulta = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_lectura, text="Lectura Actual")
        self.notebook.add(self.tab_graficas, text="Gráficas")
        self.notebook.add(self.tab_consulta, text="Últimos Datos")

        # Contenido pestaña Lectura Actual
        titulo = tk.Label(self.tab_lectura, text="Lectura Ambiental", font=("Helvetica", 16, "bold"))
        titulo.pack(pady=10)

        self.label_temp = tk.Label(self.tab_lectura, text="Temperatura: -- °C", font=("Arial", 13))
        self.label_temp.pack(pady=5)

        self.label_hum = tk.Label(self.tab_lectura, text="Humedad: -- %", font=("Arial", 13))
        self.label_hum.pack(pady=5)

        self.label_estado = tk.Label(self.tab_lectura, text="Estado: --", font=("Arial", 13, "bold"))
        self.label_estado.pack(pady=5)

        self.boton_leer = tk.Button(self.tab_lectura, text=" Leer Sensor", command=self.actualizar_datos, bg="#a8dadc", font=("Arial", 12))
        self.boton_leer.pack(pady=15)

        # Contenido pestaña Gráficas
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax_temp = self.fig.add_subplot(211)
        self.ax_hum = self.fig.add_subplot(212)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab_graficas)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)

        # Contenido pestaña Últimos Datos
        self.tabla = ttk.Treeview(self.tab_consulta, columns=("temp", "hum", "fecha", "estado"), show='headings')
        self.tabla.heading("temp", text="Temperatura (°C)")
        self.tabla.heading("hum", text="Humedad (%)")
        self.tabla.heading("fecha", text="Fecha y Hora")
        self.tabla.heading("estado", text="Estado")
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.boton_actualizar_tabla = tk.Button(self.tab_consulta, text="Actualizar Tabla", command=self.actualizar_tabla)
        self.boton_actualizar_tabla.pack(pady=5)

    def actualizar_datos(self):
        datos = self.controlador.leer_datos()
        if datos:
            temp, hum, estado = datos
            self.label_temp.config(text=f"Temperatura: {temp} °C")
            self.label_hum.config(text=f"Humedad: {hum} %")
            color_estado = "green" if estado == "Normal" else "red"
            self.label_estado.config(text=f"Estado: {estado}", fg=color_estado)
            self.actualizar_graficas()
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "Fallo al leer el sensor DHT11.")
            self.label_estado.config(text="Estado: Error", fg="gray")

    def actualizar_graficas(self):
        ultimos = self.controlador.db.cursor.execute("SELECT temperatura, humedad FROM lectura ORDER BY id_lectura DESC LIMIT 10").fetchall()
        temperaturas = [fila[0] for fila in reversed(ultimos)]
        humedades = [fila[1] for fila in reversed(ultimos)]
        indices = list(range(1, len(temperaturas)+1))

        self.ax_temp.clear()
        self.ax_temp.plot(indices, temperaturas, color="tomato", marker='o')
        self.ax_temp.set_title("Temperatura")
        self.ax_temp.set_ylabel("°C")

        self.ax_hum.clear()
        self.ax_hum.plot(indices, humedades, color="skyblue", marker='o')
        self.ax_hum.set_title("Humedad")
        self.ax_hum.set_ylabel("%")

        self.fig.tight_layout()
        self.canvas.draw()

    def actualizar_tabla(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        registros = self.controlador.db.cursor.execute("SELECT temperatura, humedad, fecha_hora, estado FROM lectura ORDER BY id_lectura DESC LIMIT 10").fetchall()
        for fila in registros:
            self.tabla.insert('', tk.END, values=fila)