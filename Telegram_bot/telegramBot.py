#Bot of telegram
import telepot

token = '564919829:AAGlguv_qCzsw03lrOwaYmEp76Y83cJB7y8';

TelegramBot = telepot.Bot(token);

print TelegramBot.getMe();
