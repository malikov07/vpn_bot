import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher, html,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums.chat_member_status import ChatMemberStatus
from customkeyboards import main_menu_keyboard,get_server_location_keyboard,get_account_menu_keyboard,get_device_keyboard,get_help_keyboard,get_referral_keyboard,get_create_bot_keyboard
from subscription import is_user_subscribed,subs_chan_keyboard

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()



@dp.message(CommandStart())
async def command_start_handler(message: Message, bot:Bot) -> None:
    """
    This handler receives messages with `/start` command
    """

    if await is_user_subscribed(message.from_user.id,bot):
        await message.answer(f"{html.bold('Откройте мир безопасности и приватности с нами!')}\n\nМы обеспечиваем защиту ваших данных, предоставляя надёжный и эффективный сервис VPN для безопасного и анонимного пользования интернетом. Ваши данные под защитой, а вы — в безопасности."
                            , reply_markup=main_menu_keyboard())
    else:
        await force_subscription(message,bot)


async def force_subscription(message: Message, bot:Bot):
    await message.answer("Чтобы продолжить пользоваться ботом, пожалуйста, выполни следующие задания! 😇", reply_markup=subs_chan_keyboard().as_markup())

@dp.callback_query(F.data.in_({"check_subs"}))
async def check_subs(callback: CallbackQuery, bot:Bot ):
    if await is_user_subscribed(callback.from_user.id, bot):
        await callback.message.answer(f"{html.bold('Откройте мир безопасности и приватности с нами!')}\n\nМы обеспечиваем защиту ваших данных, предоставляя надёжный и эффективный сервис VPN для безопасного и анонимного пользования интернетом. Ваши данные под защитой, а вы — в безопасности."
                            , reply_markup=main_menu_keyboard())
        await callback.message.delete()
        await callback.answer()
    else:
        await callback.answer("You are not subscribed to all chanels", show_alert=True)

@dp.callback_query()
async def callback_handler(callback: CallbackQuery, bot:Bot):
    if callback.data == "tariffs":
        kb = get_server_location_keyboard()
        text = "🌐 Выберите расположение сервера:\n\n❗️❓ <b>Как выбрать тариф?</b>"
        await callback.message.edit_text(text, reply_markup=kb, parse_mode="HTML")
    elif callback.data == "my_account":
        kb = get_account_menu_keyboard()
        user_id = callback.from_user.id
        bot_id = (await bot.me()).id
        balance = "0₽"  # You can replace this with actual balance from DB

        text = (
            "<b>Мой аккаунт</b>\n\n"
            f"🪪 <b>Ваш ID:</b> <code>{user_id}</code>\n"
            f"🤖 <b>ID бота:</b> <code>{bot_id}</code>\n"
            f"💰 <b>Баланс:</b> {balance}"
        )
        await callback.message.edit_text(text, reply_markup=kb, parse_mode="HTML")
    elif callback.data == "instruction":
        await callback.message.edit_text("⚡ Выберите устройство:", reply_markup=get_device_keyboard())
    elif callback.data == "help":
        await callback.message.edit_text("🆘 Помощь", reply_markup=get_help_keyboard())
    elif callback.data == "partner":
        referral_link = f"https://t.me/TunnelFoxRobot"
        text = (
            "🤝 <b>Партнерская программа</b>\n\n"
            "Получите <b>3 дня подписки</b> за каждого приглашенного друга!\n"
            "Кроме этого, вы будете получать <b>30.0%</b> от всех их покупок!\n\n"
            "<b>Условия:</b>\n"
            "1. Человек ранее не использовал бота\n"
            "2. Подключился к VPN или оплатил\n\n"
            "👨‍💻 <b>Конструктор ботов</b>\n"
            "Создайте своего собственного бота, каждый его пользователь — ваш реферал!\n\n"
            "🎁 <b>Вы пригласили:</b> 0\n"
            "📆 <b>Бонусных дней:</b> 0\n\n"
            f"🔗 <b>Ваша приглашательная ссылка:</b>\n<code>{referral_link}</code>\n"
            "*Нажмите, чтобы скопировать"
        )
        await callback.message.edit_text(text, reply_markup=get_referral_keyboard(), parse_mode="HTML")
    elif callback.data == "create_bot":
        text = (
            "🤖 <b>Создайте своего Telegram-бота за 5 минут и начните зарабатывать!</b>\n\n"
            "⚡ <b>Станьте владельцем уникального IT-бизнеса</b> — с нашим ботом вы получаете полноценный источник дохода без головной боли.\n"
            "Мы полностью берём на себя обслуживание, поддержку и технику.\n\n"
            "🛠 <b>Инструменты:</b>\n"
            "1. Рассылка сообщений\n"
            "2. Статистика, подписки, доход\n"
            "3. Управление тарифами и настройками\n"
            "4. Обязательные подписки\n"
            "5. Встроенная аналитика BotStat.io\n"
            "6. Интеграция с SubGram\n\n"
            "❓ <b>Как это работает?</b>\n"
            "1. Создаёшь VPN-бота в конструкторе\n"
            "2. Устанавливаешь наценку\n"
            "3. Пользователь оплачивает — наценка к тебе\n"
            "💵 Вывод в рублях или USDT\n\n"
            "🆘 <b>Поддержка — на нас. Доход — тебе.</b>\n"
            "Ты только привлекаешь пользователей.\n\n"
            "🧩 <b>Две партнёрские программы:</b>\n"
            "— <b>Пользовательская:</b> 30% с каждой оплаты по твоей ссылке\n"
            "— <b>Для владельцев ботов:</b> до 100% с каждой продажи даже если не твой клиент"
        )
        await callback.message.edit_text(text, reply_markup=get_create_bot_keyboard(), parse_mode="HTML")
    elif callback.data == "back_to_menu":
        text = f"{html.bold('Откройте мир безопасности и приватности с нами!')}\n\nМы обеспечиваем защиту ваших данных, предоставляя надёжный и эффективный сервис VPN для безопасного и анонимного пользования интернетом. Ваши данные под защитой, а вы — в безопасности."
                            
        await callback.message.edit_text(text, reply_markup = main_menu_keyboard())
    

    await callback.answer()

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())