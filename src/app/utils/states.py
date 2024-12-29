from aiogram.fsm.state import State, StatesGroup


class RequestStates(StatesGroup):
    in_process = State()
