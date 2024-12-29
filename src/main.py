import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramNetworkError
from aiogram.fsm.storage.redis import RedisStorage

from app.dp_settings import on_shutdown, on_startup, storage
from app.gather_routers import router
from config import bot_token


async def main() -> None:
    bot = Bot(
        token=bot_token,
        session=AiohttpSession(),
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    dp = Dispatcher(storage=RedisStorage(storage))

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, TelegramNetworkError) as error:
        if isinstance(error, TelegramNetworkError):
            logging.error('Network error')
