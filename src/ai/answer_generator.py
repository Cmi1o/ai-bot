from mistralai import Mistral, OptionalNullable

from config import mistralai_token


async def generate_answer(content: str) -> OptionalNullable[str]:
    client = Mistral(api_key=mistralai_token)

    response = await client.chat.complete_async(
        model='mistral-large-latest',
        messages = [
            {
                'role': 'user',
                'content': content,
            },
        ]
    )
    if response and response.choices:
        return response.choices[0].message.content
