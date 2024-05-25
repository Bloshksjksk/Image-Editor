# By @TroJanzHEX
from googletrans import Translator
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from config import Config


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        if Config.PRIVATE is True and message.chat.username not in Config.USERNAMES:
            await message.reply_text(Translator().translate(f"Hi {message.chat.first_name} you are not allowed to use this bot!", dest=Config.LANG).text, quote=True)
        else:
            await client.send_message(
                chat_id=message.chat.id,
                text=Translator().translate("🎨Select your required mode from below!🎨", dest=Config.LANG).text,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text=Translator().translate('💡BRIGHT💡', dest=Config.LANG).text, callback_data="bright"),
                            InlineKeyboardButton(text=Translator().translate('🌇MIXED🌇', dest=Config.LANG).text, callback_data="mix"),
                            InlineKeyboardButton(text=Translator().translate('▫️B&W▪️', dest=Config.LANG).text, callback_data="b|w"),
                        ],
                        [
                            InlineKeyboardButton(text=Translator().translate('⭕CIRCLE⭕', dest=Config.LANG).text, callback_data="circle"),
                            InlineKeyboardButton(text=Translator().translate('🛡️BLUR🛡️', dest=Config.LANG).text, callback_data="blur"),
                            InlineKeyboardButton(text=Translator().translate('🖼️BORDER🖼️', dest=Config.LANG).text, callback_data="border"),
                        ],
                        [
                            InlineKeyboardButton(text=Translator().translate('〽️STICKER〽️', dest=Config.LANG).text, callback_data="stick"),
                            InlineKeyboardButton(text=Translator().translate('🌀ROTATE🌀', dest=Config.LANG).text, callback_data="rotate"),
                            InlineKeyboardButton(text=Translator().translate('🔆CONTRAST🔆', dest=Config.LANG).text, callback_data="contrast"),
                        ],
                        [
                            InlineKeyboardButton(text=Translator().translate('🟤SEPIA🟤', dest=Config.LANG).text, callback_data="sepia"),
                            InlineKeyboardButton(text=Translator().translate('✏️PENCIL✏️', dest=Config.LANG).text, callback_data="pencil"),
                            InlineKeyboardButton(text=Translator().translate('🧒CARTOON🧒', dest=Config.LANG).text, callback_data="cartoon"),
                        ],
                        [
                            InlineKeyboardButton(text=Translator().translate('🙃INVERT🙃', dest=Config.LANG).text, callback_data="inverted"),
                            InlineKeyboardButton(text=Translator().translate('🪩GLITCH🪩', dest=Config.LANG).text, callback_data="glitch"),
                            InlineKeyboardButton(
                                text=Translator().translate('🕳️REMOVE BG🕳️', dest=Config.LANG).text, callback_data="removebg"
                            ),
                        ],
                        [
                            InlineKeyboardButton(text=Translator().translate('🚪CLOSE🚪', dest=Config.LANG).text, callback_data="close_e"),
                            InlineKeyboardButton(text=Translator().translate('📔COVER📔', dest=Config.LANG).text, callback_data="cover"),
                        ],
                    ]
                ),
                reply_to_message_id=message.id,
            )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text(Translator().translate('Something went wrong! Contact @fligher', dest=Config.LANG).text, quote=True)
            except Exception:
                return
