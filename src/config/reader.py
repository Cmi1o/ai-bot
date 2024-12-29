from typing import Final as const

from .loader import settings

__all__ = ('bot_token', 'mistralai_token', 'redis_url')


bot_token: const = settings.bot_token.get_secret_value()
mistralai_token: const = settings.mistralai_token.get_secret_value()
redis_url: const = settings.redis_url.get_secret_value()
