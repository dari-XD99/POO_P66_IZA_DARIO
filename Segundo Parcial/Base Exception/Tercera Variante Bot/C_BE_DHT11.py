from M_BE_DHT11 import ModeloDHT11
import threading
import time
from telegram.ext import Updater, CommandHandler

class ComandoInvalidoError(Exception):
    pass

class ControladorDHT11:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)
        self.token = "7931784865:AAESjqpTO2Yx62fe1xyCGu0wm9ERnYMaAlQ"
        self.chat_id = None
        self.updater = Updater(token=self.token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler("Encender", self.cmd_encender))
        dp.add_handler(CommandHandler("Apagar", self.cmd_apagar))
        dp.add_handler(CommandHandler("Estado", self.cmd_estado))
        dp.add_handler(CommandHandler("Boton", self.cmd_boton))

    def procesar_comando(self, comando):
        try:
            if comando == "/Estado":
                self.enviar_estado()
            elif comando == "/Encender":
                self.modelo.desactivar_control_por_boton()
                self.modelo.encender_led()
                self.vista.actualizar_estado_led(True)
            elif comando == "/Apagar":
                self.modelo.desactivar_control_por_boton()
                self.modelo.apagar_led()
                self.vista.actualizar_estado_led(False)
            elif comando == "/Boton":
                self.activar_modo_boton()
            else:
                raise ComandoInvalidoError()
        except ComandoInvalidoError:
            self.vista.mostrar_mensajes("Comando Invalido", "Comando Invalido")
            self.vista.mostrar_datos("---", "---")

    def cmd_encender(self, update, context):
        self.modelo.desactivar_control_por_boton()
        self.modelo.encender_led()
        self.vista.actualizar_estado_led(True)

    def cmd_apagar(self, update, context):
        self.modelo.desactivar_control_por_boton()
        self.modelo.apagar_led()
        self.vista.actualizar_estado_led(False)

    def cmd_estado(self, update, context):
        temp, hum = self.modelo.leer_datos()
        if temp is None or hum is None:
            mensaje_temp = mensaje_hum = "Error al leer el sensor"
            respuesta = f"{mensaje_temp}\n{mensaje_hum}"
        else:
            mensaje_temp = "Enciende el Calefactor" if temp < 20 else "Enciende el Ventilador"
            mensaje_hum = "Enciende el Humidificador" if hum < 40 else "Enciende el Deshumidificador"
            respuesta = f"Temperatura: {temp}°C\nHumedad: {hum}%\n{mensaje_temp}\n{mensaje_hum}"
        update.message.reply_text(respuesta)
        self.vista.mostrar_mensajes(mensaje_temp, mensaje_hum)
        self.vista.mostrar_datos(temp, hum)

    def cmd_boton(self, update, context):
        self.activar_modo_boton()

    def activar_modo_boton(self):
        self.modelo.activar_control_por_boton()

    def ejecutar(self):
        threading.Thread(target=self.controlar_boton, daemon=True).start()
        threading.Thread(target=self.updater.start_polling, daemon=True).start()

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