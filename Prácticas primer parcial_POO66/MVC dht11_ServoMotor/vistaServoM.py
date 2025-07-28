from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

class VistaBot:
    def __init__(self, controlador):
        self.controlador = controlador
        self.app = ApplicationBuilder().token('Aqui token').build()

    async def start(self, update: Update, context: CallbackContext) -> None:
        print("Comando /start recibido.")
        await update.message.reply_text('¡Hola! Estoy listo para mostrarte la temperatura, humedad y mover el servomotor si es necesario.')

    async def status(self, update: Update, context: CallbackContext) -> None:
        temp, hum = self.controlador.obtener_datos()
        if temp is not None and hum is not None:
            await update.message.reply_text(f"Temperatura: {temp}°C |Humedad: {hum}%")
        else:
            await update.message.reply_text("Error al obtener datos del sensor.")

    def iniciar(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("status", self.status))
        print("Bot iniciado... esperando comandos...")
        self.app.run_polling()
