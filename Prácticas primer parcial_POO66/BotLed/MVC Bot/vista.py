class TelegramView:
    def __init__(self, bot):
        self.bot = bot

    def send_message(self, chat_id, message):
        self.bot.sendMessage(chat_id, message)

