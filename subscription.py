from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.utils.keyboard import InlineKeyboardBuilder


REQUIRED_CHANNELS = {
    "NewUU community": "@newuu_community"
}


def subs_chan_keyboard():
    # it is the function that returns keyboard to subscription
    builder = InlineKeyboardBuilder()
    for name, chanel in REQUIRED_CHANNELS.items():
        builder.button(text=f"{name}", url=f"t.me/{chanel[1:]}",callback_data="chanel")
    builder.button(text="✅Я выполнил", callback_data="check_subs")
    builder.adjust(1)
    return builder



# Function to check if user is subscribed
async def is_user_subscribed(user_id,bot):
    for name, channel in REQUIRED_CHANNELS.items():
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        if member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR]:
            return False
        
    return True