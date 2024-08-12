from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv



load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()


async def set_bot_commands():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="picture", description="Получите картику"),
        types.BotCommand(command="myinfo", description="Моя инфа"),
        types.BotCommand(command="random_recipe", description="Рандомный рецепт"),
        types.BotCommand(command="dishes", description="Еда")
    ])