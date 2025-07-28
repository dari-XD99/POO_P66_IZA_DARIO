import telepot
from telepot.loop import MessageLoop
import time

from modelo import LedModel
from vista import TelegramView

class BotController:
    def __init__(self, token, led_pin):
        self.led = LedModel(led_pin)
        self.bot = telepot.Bot(token)
        self.view = TelegramView(self.bot)

        MessageLoop(self.bot, self.action).run_as_thread()
        print('Bot is up and running...')

    def action(self, msg):
        chat_id = msg['chat']['id']
        command = msg.get('text', '')

        print(f'Received: {command}')

        if 'on' in command.lower():
            if 'led' in command.lower():
                self.led.turn_on()
                self.view.send_message(chat_id, "Turned on LED")

        elif 'off' in command.lower():
            if 'led' in command.lower():
                self.led.turn_off()
                self.view.send_message(chat_id, "Turned off LED")

    def run(self):
        while True:
            time.sleep(10)
