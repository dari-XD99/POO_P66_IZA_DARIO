from controlador import BotController

if __name__ == "__main__":
    TOKEN = 'Aquí token'
    LED_PIN = 18

    bot_controller = BotController(TOKEN, LED_PIN)
    bot_controller.run()
