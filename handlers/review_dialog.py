from aiogram import F, Router, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@dialog_router.message(Command("feedback"))
async def start_dialog(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await message.answer("Как Вас зовут?")


@dialog_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Ваш номер телефона?")


@dialog_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    # if not age.isdigit():
    #     await message.answer("Вводите только цифры")
    #     return
    # age = int(age)
    # if age < 12 or age > 90:
    #     await message.answer("Вводите числа от 12 до 90!")
    #     return
    await state.update_data(phone_number=phone_number)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата визита?")


@dialog_router.message(RestourantReview.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)
    await message.answer("Качество еды?")


@dialog_router.message(RestourantReview.food_rating)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(food_rating=message.text)
    await state.set_state(RestourantReview.cleanliness_rating)
    await message.answer("Качество чистоты?")


@dialog_router.message(RestourantReview.cleanliness_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Отзыв в целом?")


@dialog_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("Спасибо за отзыв!")
    data = await state.get_data()
    print(data)

    await state.clear()