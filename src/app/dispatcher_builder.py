from aiogram import Bot


async def on_startup(bot: Bot) -> None:
    await bot.delete_webhook()


async def on_shutdown(bot: Bot) -> None:
    print(f'Bot({await bot.get_my_name()}, id={bot.id}) finished polling')
