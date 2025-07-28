import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class InterfazMonitor:
    def __init__(self, root, controlador):
        self.root = root
        self.controlador = controlador
        self.root.title("Monitor DHT11 - GPIO4")
        self.root.geometry("800x600")
        
        self._crear_interfaz()
        self.actualizar_datos()
    
    def _crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Panel de control
        control_frame = ttk.LabelFrame(main_frame, text="Control - Sensor en GPIO4", padding="10")
        control_frame.pack(fill=tk.X)
        
        ttk.Button(
            control_frame, 
            text="Iniciar Monitoreo", 
            command=self.controlador.iniciar_monitoreo
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            control_frame, 
            text="Detener Monitoreo", 
            command=self.controlador.detener_monitoreo
        ).pack(side=tk.LEFT, padx=5)
        
        # Gráficos
        self._crear_graficos(main_frame)
        
        # Tabla de lecturas
        self._crear_tabla(main_frame)
    
    # ... (resto del código de la vista igual que antes)
