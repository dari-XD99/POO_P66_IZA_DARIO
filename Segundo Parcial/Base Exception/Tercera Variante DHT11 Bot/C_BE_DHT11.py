from M_BE_DHT11 import ModeloDHT11
import threading
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class ComandoInvalidoError(Exception):
    pass

class ControladorDHT11:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.set_controlador(self)

        self.token = "Token"
        self.updater = Updater(token=self.token, use_context=True)
        dp = self.updater.dispatcher
        dp.add_handler(CommandHandler("Encender", self.cmd_encender))
        dp.add_handler(CommandHandler("Apagar", self.cmd_apagar))
        dp.add_handler(CommandHandler("Estado", self.cmd_estado))
        dp.add_handler(CommandHandler("Boton", self.cmd_boton))
        dp.add_handler(MessageHandler(Filters.text & (~Filters.command), self.cmd_invalido))
        dp.add_handler(MessageHandler(Filters.command, self.cmd_invalido))

    def procesar_comando(self, comando):
        try:
            if comando == "/Estado":
                self.ejecutar_estado()
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

    def ejecutar_estado(self, chat_callback=None):
        temp, hum = self.modelo.leer_datos()
        if temp is None or hum is None:
            mensaje_temp = mensaje_hum = "Error al leer el sensor"
        else:
            mensaje_temp = ""
            if temp < 20:
                mensaje_temp = "Enciende el Calefactor"
            elif temp > 25:
                mensaje_temp = "Enciende el Ventilador"

            mensaje_hum = ""
            if hum < 40:
                mensaje_hum = "Enciende el Humidificador"
            elif hum > 46:
                mensaje_hum = "Enciende el Deshumidificador"

        self.vista.mostrar_mensajes(mensaje_temp or "", mensaje_hum or "")
        if temp is not None and hum is not None:
            self.vista.mostrar_datos(temp, hum)

        if chat_callback:
            mensaje = f"Temperatura: {temp}°C\nHumedad: {hum}%"
            if mensaje_temp:
                mensaje += f"\n{mensaje_temp}"
            if mensaje_hum:
                mensaje += f"\n{mensaje_hum}"
            chat_callback(mensaje)
        elif temp is None or hum is None:
            self.vista.mostrar_datos("---", "---")

    def cmd_encender(self, update, context):
        self.modelo.desactivar_control_por_boton()
        self.modelo.encender_led()
        self.vista.actualizar_estado_led(True)
        context.bot.send_message(chat_id=update.effective_chat.id, text="LED encendido")

    def cmd_apagar(self, update, context):
        self.modelo.desactivar_control_por_boton()
        self.modelo.apagar_led()
        self.vista.actualizar_estado_led(False)
        context.bot.send_message(chat_id=update.effective_chat.id, text="LED apagado")

    def cmd_estado(self, update, context):
        self.ejecutar_estado(lambda msg: context.bot.send_message(chat_id=update.effective_chat.id, text=msg))

    def cmd_boton(self, update, context):
        self.activar_modo_boton()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Modo botón activado")

    def cmd_invalido(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Comando Invalido")

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