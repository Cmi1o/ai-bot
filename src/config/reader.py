from typing import Final as const

from .loader import settings


__all__ = (
    'bot_token',
    'mistralai_token',
)


bot_token: const = settings.bot_token.get_secret_value()
mistralai_token: const = settings.mistralai_token.get_secret_value()
