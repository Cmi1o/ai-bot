from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()

@router.message(CommandStart(ignore_case=True))
async def start(message: Message) -> None:
    enter_message = 'ERROR'
    
    if message.from_user:
        enter_message = (
            f'Привет, {message.from_user.full_name}, я ИИ на подобие ChatGPT. Пришли '
            'свой запрос'
        )
    
    await message.reply(enter_message)
