from aiogram.fsm.state import StatesGroup, State


class RequestStates(StatesGroup):
    in_process = State()
