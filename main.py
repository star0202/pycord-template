from dotenv import load_dotenv

load_dotenv(".env")

from classes import Bot  # noqa: E402

if __name__ == "__main__":
    bot = Bot()
    bot.run()
