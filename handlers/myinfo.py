from aiogram import Router, types, F
from aiogram.filters.command import Command

myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo_command_handler(message: types.Message):
    await message.answer(f"Ваш id: {message.from_user.id},\n"
                         f"Ваш first_name: {message.from_user.first_name},\n"
                         f"Ваш username: {message.from_user.username} \n\n")