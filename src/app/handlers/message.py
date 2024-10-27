from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.utils.states import RequestStates
from ai import generate_answer


router = Router()

@router.message(RequestStates.in_process)
async def in_process(message: Message) -> None:
    await message.answer('Можно сделать только один запрос за раз')


@router.message(F.text)
async def generate_response(message: Message, state: FSMContext) -> None:
    await state.set_state(RequestStates.in_process)
    
    await message.answer('Подождите идет генерация ответа...')
    try:
        await message.reply(await generate_answer(message.text))  # type: ignore
    except:
        await message.reply('Произошла ошибка во время генерации ответа')
    
    await state.clear()


@router.message(~F.text)
async def unknown_format(message: Message) -> None:
    await message.answer('Отправлен неизвестный формат, бот обрабатывает только текст')
