import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramNetworkError

from src.config import bot_token
from src.app.gather_routers import router


async def main() -> None:
    bot = Bot(bot_token, parse_mode=ParseMode.MARKDOWN)
    dp = Dispatcher()
    
    dp.include_router(router)
    
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, TelegramNetworkError):
        print('Bot stopped')
