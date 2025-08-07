from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder



def main_menu_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💎Тарифы", callback_data="tariffs")],

            [InlineKeyboardButton(text="🔑Мои ключи", callback_data="my_keys"),InlineKeyboardButton(text="⚙️Мой аккаунт", callback_data="my_account")],
            
            [InlineKeyboardButton(text="📚Инструкция", callback_data="instruction"),InlineKeyboardButton(text="🛟Помощь", callback_data="help")],
            
            [InlineKeyboardButton(text="🤝Партнерам", callback_data="partner"),InlineKeyboardButton(text="🤖Создать бот", callback_data="create_bot")],
            
        ]
    )


def get_server_location_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🆓 Получить пробную версию",
        callback_data="get_trial"
    )
    builder.button(
        text="🌐 Мульти — 449 ₽/мес",
        callback_data="multi_449"
    )
    builder.button(
        text="🇷🇺 Россия [YT, INST, DS] — 75 ₽/мес",
        callback_data="russia_75"
    )
    builder.button(
        text="🇳🇱 Нидерланды — 149 ₽/мес",
        callback_data="netherlands_149"
    )
    builder.button(
        text="🇩🇪 Германия — 224 ₽/мес",
        callback_data="germany_224"
    )
    builder.button(
        text="🇫🇷 Франция — 299 ₽/мес",
        callback_data="france_299"
    )
    builder.button(
        text="🇺🇸 США — 329 ₽/мес",
        callback_data="usa_329"
    )
    builder.button(
        text="🔙 Вернуться",
        callback_data="back_to_menu"
    )

    builder.adjust(1)  # One button per row
    return builder.as_markup()


def get_account_menu_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text="🎁 Активировать промокод",
        callback_data="activate_promo"
    )
    builder.button(
        text="🔙 Вернуться",
        callback_data="back_to_menu"
    )

    builder.adjust(1)  # One button per row
    return builder.as_markup()

def get_device_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="📱 Android", callback_data="device_android"),
        InlineKeyboardButton(text="💻 Windows", callback_data="device_windows"),
    )
    builder.row(
        InlineKeyboardButton(text="🍎 Iphone", callback_data="device_iphone"),
        InlineKeyboardButton(text="🍏 Mac", callback_data="device_mac"),
    )
    builder.row(
        InlineKeyboardButton(text="🔙 Вернуться", callback_data="back_to_menu")
    )
    return builder.as_markup()


def get_help_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="❗ Часто задаваемые вопросы", callback_data="faq"))
    builder.row(InlineKeyboardButton(text="📩 Написать в поддержку", callback_data="v"))
    builder.row(InlineKeyboardButton(text="📃 Пользовательское соглашение", callback_data="b"))
    builder.row(InlineKeyboardButton(text="🔙 Вернуться", callback_data="back_to_menu"))
    return builder.as_markup()


def get_referral_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📤 Отправить друзьям Telegram",callback_data="b" ))
    builder.row(InlineKeyboardButton(text="📤 Отправить друзьям WhatsApp",callback_data="b" ))
    builder.row(InlineKeyboardButton(text="🤖 Конструктор ботов", callback_data="bot_builder"))
    builder.row(InlineKeyboardButton(text="🔙 Вернуться", callback_data="back_to_menu"))
    return builder.as_markup()

def get_create_bot_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="создать бот", callback_data="b"))
    builder.row(InlineKeyboardButton(text="🔙 Вернуться", callback_data="back_to_menu"))
    return builder.as_markup()