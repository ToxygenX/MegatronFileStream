import time
from .vars import Var
from .bot import StreamBot

print('\n')
print('------------------- Initalizing Telegram Bot -------------------')

StreamBot.start()
bot_info = StreamBot.get_me()

__version__ = 1.08
StartTime = time.time()
