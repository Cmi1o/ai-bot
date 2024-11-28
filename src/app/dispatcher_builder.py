import logging

from aiogram import Bot
from aiogram.types import BotName


__all__ = (
    'on_startup',
    'on_shutdown'
)

logger = logging.Logger(__name__, level=logging.INFO)


class LogBot:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    async def get_name(self) -> BotName:
        return await self.bot.get_my_name()
    
    async def in_log(self) -> str:
        return f'bot({await self.get_name()}, id={self.bot.id})'


async def on_startup(bot: Bot) -> None:
    bot_in_log = await LogBot(bot).in_log()
    
    await bot.delete_webhook()
    logger.info(f'Started polling for {bot_in_log}')


async def on_shutdown(bot: Bot) -> None:
    bot_in_log = await LogBot(bot).in_log()
    
    logger.info(f'Finished polling for {bot_in_log}')
