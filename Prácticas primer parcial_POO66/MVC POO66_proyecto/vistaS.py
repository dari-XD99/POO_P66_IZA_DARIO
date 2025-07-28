from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

class VistaBot:
    def __init__(self, controlador):
        self.controlador = controlador
        self.app = ApplicationBuilder().token("Aqui Token").build()

    async def start(self, update: Update, context: CallbackContext) -> None:
        await update.message.reply_text("Bot listo. Usa /status, /suelo, /abrir o /cerrar.")

    async def status(self, update: Update, context: CallbackContext) -> None:
        temp, hum = self.controlador.obtener_datos_ambiente()
        if temp is not None:
            await update.message.reply_text(f"Temp: {temp}°C | Humedad: {hum}%")
        else:
            await update.message.reply_text("No se pudo leer el sensor DHT11.")

    async def suelo(self, update: Update, context: CallbackContext) -> None:
        seco = self.controlador.obtener_estado_suelo()
        estado = "SECO" if seco else "HÚMEDO"
        await update.message.reply_text(f"Estado del suelo: {estado}")

    async def abrir(self, update: Update, context: CallbackContext) -> None:
        self.controlador.abrir_ventana()
        await update.message.reply_text("Ventana abierta (servo 180°)")

    async def cerrar(self, update: Update, context: CallbackContext) -> None:
        self.controlador.cerrar_ventana()
        await update.message.reply_text("Ventana cerrada (servo 0°)")

    def iniciar(self):
        self.app.add_handler(CommandHandler("start", self.start))
        self.app.add_handler(CommandHandler("status", self.status))
        self.app.add_handler(CommandHandler("suelo", self.suelo))
        self.app.add_handler(CommandHandler("abrir", self.abrir))
        self.app.add_handler(CommandHandler("cerrar", self.cerrar))

        print("Bot Telegram en línea.")
        self.app.run_polling()
