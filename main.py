from dotenv import load_dotenv

from classes import Bot

load_dotenv(".env")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
