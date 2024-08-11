from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_router = Router()


@start_router.message(Command("start"))
async def start_command_handler(message: types.Message):
    # print(vars(message.from_user))
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://geeks.kg"),
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Вакансии", callback_data="vacancies")
            ],
            [
                types.InlineKeyboardButton(text="Контакты", callback_data="contaks")
            ]
        ]
    )
    await message.answer(f"Привет, {message.from_user.first_name}, я бот ресторана 'Пишпек' ", reply_markup=kb)


# @start_router.callback_query(lambda callback: callback.data == "about_us")
@start_router.callback_query(F.data == "about_us")
async def aboutus_handler(callback: types.CallbackQuery):
    # await callback.answer("опвлплвповло")
    await callback.message.answer("ООО 'Пишпек', 2020 ")


@start_router.callback_query(F.data == "vacancies")
async def vacancies_handler(callback: types.CallbackQuery):
    # await callback.answer("опвлплвповло")
    await callback.message.answer("В данный момент нет открытых вакансий")

@start_router.callback_query(F.data == "contaks")
async def contaks_handler(callback: types.CallbackQuery):
    # await callback.answer("опвлплвповло")
    await callback.message.answer("Телефон: +996 555 555 555, Адрес: г. Бишкек, ул. Ленина, д. 1 ")


@start_router.message(F.text == "Детектив")
async def detective_handler(message: types.Message):
    await message.answer("Книги жанра Детектив")