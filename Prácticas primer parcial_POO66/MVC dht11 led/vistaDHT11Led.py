from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

class VistaBot:
    def __init__(self, controlador):
        self.controlador = controlador
        self.app = ApplicationBuilder().token('Aqui token').build()

    async def start(self, update: Update, context: CallbackContext) -> None:
        """Respuesta al comando /start"""
        print("Comando /start recibido.")
        await update.message.reply_text('¡Hola! Estoy listo para mostrarte la temperatura y la humedad.')

    async def status(self, update: Update, context: CallbackContext) -> None:
        """Muestra la temperatura y la humedad"""
        temp, hum = self.controlador.obtener_datos()
        if temp is not None and hum is not None:
            await update.message.reply_text(f"Temperatura: {temp}°C | Humedad: {hum}%")
        else:
            await update.message.reply_text("Error al obtener los datos del sensor.")

    def iniciar(self):
        """Inicia el bot de Telegram para escuchar los comandos"""
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("status", self.status))
        print("Bot iniciado... esperando comandos...")
        self.app.run_polling()
