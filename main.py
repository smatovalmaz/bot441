import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
import logging
import glob
import random
import os


load_dotenv()
token = getenv("BOT_TOKEN")
bot = Bot(token=token)
dp = Dispatcher()

recipes = [
    "Паста с помидорами и базиликом:\n\nИнгредиенты: паста, помидоры, чеснок, оливковое масло, базилик.\nПриготовление: Отварите пасту. На сковороде обжарьте чеснок в оливковом масле, добавьте помидоры, тушите до мягкости. Смешайте с пастой и добавьте базилик.",
    "Омлет с овощами:\n\nИнгредиенты: яйца, молоко, помидоры, шпинат, соль, перец.\nПриготовление: Взбейте яйца с молоком, вылейте в сковороду, добавьте нарезанные помидоры и шпинат, готовьте до полной готовности.",
    "Цезарь салат:\n\nИнгредиенты: куриное филе, салат Ромен, пармезан, гренки, соус Цезарь.\nПриготовление: Обжарьте курицу, нарежьте её и смешайте с нарезанным салатом, добавьте гренки и тертый пармезан, полейте соусом.",
    "Чили кон карне:\n\nИнгредиенты: говяжий фарш, фасоль, помидоры, лук, специи.\nПриготовление: Обжарьте лук и фарш, добавьте помидоры и фасоль, тушите с приправами до готовности.",
    "Смузи с бананом и ягодами:\n\nИнгредиенты: банан, замороженные ягоды, йогурт, мед.\nПриготовление: Смешайте все ингредиенты в блендере до получения однородной массы."
]

@dp.message(Command("start"))
async def start_command_handler(message: types.Message):
    # print(vars(message.from_user))
    await message.answer(f"Привет, {message.from_user.first_name}, я бот Группы 44-1")


@dp.message(Command("myinfo"))
async def myinfo_command_handler(message: types.Message):
    await message.answer(f"Ваш id: {message.from_user.id},\n"
                         f"Ваш first_name: {message.from_user.first_name},\n"
                         f"Ваш username: {message.from_user.username} \n\n")


@dp.message(Command("radom_recipe"))
async def random_recipe(message: types.Message):
    recipe = random.choice(recipes)
    await message.answer(recipe)


@dp.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())