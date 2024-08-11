from aiogram import Router, types, F
from aiogram.filters.command import Command


dishes_router = Router()



@dishes_router.message(F.text == "Холодные напитки")
async def picture_handler(message: types.Message):
    image = types.FSInputFile("images/mohito.jpg")
    await message.answer_photo(
        photo=image,
        caption="Мохито"
    )


@dishes_router.message(F.text == "Десерты")
async def picture_handler(message: types.Message):
    image = types.FSInputFile("images/cheescaik.jpg")
    await message.answer_photo(
        photo=image,
        caption="Чискейк"
    )