import time
import threading

class ControladorLed:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.modo = "boton"
        self.ejecutando = True

    def monitorear_comandos(self):
        while self.ejecutando:
            comando = input("> ")
            try:
                if comando == "/EncenderLed":
                    self.modelo.encender_led()
                    self.vista.mostrar_estado_led(True)
                    self.modo = "comando"
                    self.vista.mostrar_modo(self.modo)

                elif comando == "/ApagarLed":
                    self.modelo.apagar_led()
                    self.vista.mostrar_estado_led(False)
                    self.modo = "comando"
                    self.vista.mostrar_modo(self.modo)

                elif comando == "/Boton":
                    self.modo = "boton"
                    self.vista.mostrar_modo(self.modo)

                else:
                    raise ValueError("Comando inválido")

            except Exception:
                self.vista.mostrar_error_comando()

    def ejecutar(self):
        hilo_comandos = threading.Thread(target=self.monitorear_comandos)
        hilo_comandos.daemon = True
        hilo_comandos.start()

        try:
            while True:
                if self.modo == "boton":
                    if self.modelo.leer_boton():
                        if not self.modelo.obtener_estado_led():
                            self.modelo.encender_led()
                            self.vista.mostrar_estado_led(True)
                    else:
                        if self.modelo.obtener_estado_led():
                            self.modelo.apagar_led()
                            self.vista.mostrar_estado_led(False)
                time.sleep(0.1)

        except KeyboardInterrupt:
            self.ejecutando = False
            print("Programa finalizado por el usuario.")
