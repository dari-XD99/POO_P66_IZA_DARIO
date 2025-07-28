from M_BE_DHT11 import ModeloDHT11
import threading
import time
from telegram.ext import Updater, CommandHandler

class ComandoInvalidoError(Exception):
    pass

class EstadoTemp(Exception):
    pass

class EstadoHum(Exception):
    pass

class ControladorDHT11:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.token = "token telegram"
        self.chat_id = None

    def procesar_comando(self, comando):
        try:
            if comando == "/Estado":
                temp, hum = self.modelo.leer_datos()
                if temp is None or hum is None:
                    raise ValueError("Error al leer el sensor")

                if temp < 20:
                    raise EstadoTemp("Enciende el Calefactor")
                else:
                    raise EstadoTemp("Enciende el Ventilador")

                if hum < 40:
                    raise EstadoHum("Enciende el Humidificador")
                else:
                    raise EstadoHum("Enciende el Deshumidificador")

            elif comando == "/Encender":
                self.modelo.desactivar_control_por_boton()
                self.modelo.encender_led()
                self.vista.actualizar_estado_led(True)

            elif comando == "/Apagar":
                self.modelo.desactivar_control_por_boton()
                self.modelo.apagar_led()
                self.vista.actualizar_estado_led(False)

            else:
                raise ComandoInvalidoError()

        except ValueError:
            self.vista.mostrar_mensajes("Error al leer el sensor", "Error al leer el sensor")
            self.vista.mostrar_datos("---", "---")

        except EstadoTemp as e:
            mensaje_temp = str(e)
            temp, hum = self.modelo.leer_datos()
            mensaje_hum = "Enciende el Humidificador" if hum < 40 else "Enciende el Deshumidificador"
            self.vista.mostrar_mensajes(mensaje_temp, mensaje_hum)
            self.vista.mostrar_datos(temp, hum)

        except EstadoHum as e:
            mensaje_hum = str(e)
            temp, hum = self.modelo.leer_datos()
            mensaje_temp = "Enciende el Calefactor" if temp < 20 else "Enciende el Ventilador"
            self.vista.mostrar_mensajes(mensaje_temp, mensaje_hum)
            self.vista.mostrar_datos(temp, hum)

        except ComandoInvalidoError:
            self.vista.mostrar_mensajes("Comando Invalido", "Comando Invalido")
            self.vista.mostrar_datos("---", "---")

    def activar_modo_boton(self):
        self.modelo.activar_control_por_boton()

    def ejecutar(self):
        hilo = threading.Thread(target=self.controlar_boton, daemon=True)
        hilo.start()

    def controlar_boton(self):
        while True:
            if self.modelo.esta_en_modo_boton():
                if self.modelo.leer_boton():
                    self.modelo.apagar_led()
                    self.vista.actualizar_estado_led(False)
                else:
                    self.modelo.encender_led()
                    self.vista.actualizar_estado_led(True)
            time.sleep(0.1)