from utils.bot import Bot
from dotenv import load_dotenv

load_dotenv(".env")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
