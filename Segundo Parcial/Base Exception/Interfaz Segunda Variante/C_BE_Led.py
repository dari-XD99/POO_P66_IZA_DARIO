import time
import threading

class ControladorLed:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.modo = "comando"
        self.ejecutando = True

    def ejecutar(self):
        hilo = threading.Thread(target=self.bucle_principal)
        hilo.daemon = True
        hilo.start()

    def bucle_principal(self):
        while self.ejecutando:
            if self.modo == "boton":
                if self.modelo.leer_boton():
                    if not self.modelo.obtener_estado_led():
                        self.modelo.encender_led()
                        self.vista.actualizar_estado_led(True)
                else:
                    if self.modelo.obtener_estado_led():
                        self.modelo.apagar_led()
                        self.vista.actualizar_estado_led(False)
            time.sleep(0.1)

    def procesar_comando(self, comando):
        if comando == "/Encender":
            self.modelo.encender_led()
            self.vista.actualizar_estado_led(True)
            self.modo = "comando"
            self.vista.actualizar_modo("COMANDO")
        elif comando == "/Apagar":
            self.modelo.apagar_led()
            self.vista.actualizar_estado_led(False)
            self.modo = "comando"
            self.vista.actualizar_modo("COMANDO")
        else:
            self.vista.mostrar_error_comando()

    def activar_modo_boton(self):
        self.modo = "boton"
        self.vista.actualizar_modo("BOTÓN")
