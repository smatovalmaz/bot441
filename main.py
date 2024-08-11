import asyncio

import logging


from bot_config import bot, dp
from handlers.echo import echo_router
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import random_recipe_router
from handlers.dishes import dishes_router





async def main():
    # добавляем маршрутизаторы диспетчеру
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(random_recipe_router)
    dp.include_router(dishes_router)

    # в самом конце
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())