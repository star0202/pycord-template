from dotenv import load_dotenv

from utils.bot import Bot

load_dotenv(".env")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
