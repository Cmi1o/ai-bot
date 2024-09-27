from aiogram import Router

from src.app.handlers import command, message


def gather_routers(*routers) -> Router:
    router = Router()
    router.include_routers(*routers)
    
    return router


router = gather_routers(
    command.router,
    message.router
)
