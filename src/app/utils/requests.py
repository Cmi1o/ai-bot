import aiohttp

from src.config import bot_token


__all__ = (
    'send_message',
    'base_url',
    'url'
)


base_url = f'https://api.telegram.org/bot'

def url(bot_token: str) -> str:
    return base_url + bot_token


async def send_message(text: str) -> aiohttp.ClientResponse:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=f'{url(bot_token)}/sendMessage', 
            json={'text': text}
        ) as response:
            return response
