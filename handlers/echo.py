from aiogram import Router, types


echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.reply(message.text)