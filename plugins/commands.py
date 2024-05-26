# By @TroJanzHEX
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters
from script import script  # pylint:disable=import-error
from googletrans import Translator
from config import Config



@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    member = await client.get_chat_member(Config.CHANNELS, message.from_user.id)
    try:
        if Config.PRIVATE is True and message.chat.username not in Config.USERNAMES:
            await message.reply_text(Translator().translate(f"Hi {message.chat.first_name} you are not allowed to use this bot!", dest=Config.LANG).text, quote=True)
            
        if member.status not in ["creator", "administrator", "member"]:
            await message.reply_text("You must be a member of the specified channel to use this bot. Please join the channel and try again @movie_time_botonly.")
            
        else:
            await message.reply_text(
                text=script.START_MSG.format(message.from_user.mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(Translator().translate('🖲️HELP🖲️', dest=Config.LANG).text, callback_data="help_data"),
                            InlineKeyboardButton(Translator().translate('🧑‍💻ABOUT🧑‍💻', dest=Config.LANG).text, callback_data="about_data"),
                        ],
                        [
                            InlineKeyboardButton(
                                Translator().translate('🏆TRUMBOTS🏆', dest=Config.LANG).text,
                                url="https://t.me/movie_time_botonly",
                            )
                        ],
                    ]
                ),
                reply_to_message_id=message.id,
            )
    except Exception:
        pass


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    member = await client.get_chat_member(Config.CHANNELS, message.from_user.id)
    try:
        if Config.PRIVATE is True and message.chat.username not in Config.USERNAMES:
            await message.reply_text(Translator().translate(f"Hi {message.chat.first_name} you are not allowed to use this bot!", dest=Config.LANG).text, quote=True)
        
        if member.status not in ["creator", "administrator", "member"]:
            await message.reply_text("You must be a member of the specified channel to use this bot. Please join the channel and try again.")
        else:
            await message.reply_text(
                text=script.HELP_MSG,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(Translator().translate('🔙BACK🔙', dest=Config.LANG).text, callback_data="start_data"),
                            InlineKeyboardButton(Translator().translate('🧑‍💻ABOUT🧑‍💻', dest=Config.LANG).text, callback_data="about_data"),
                        ],
                        [
                            InlineKeyboardButton(
                                Translator().translate('🏆TRUMBOTS🏆', dest=Config.LANG).text,
                                url="https://t.me/movie_time_botonly",
                            )
                        ],
                    ]
                ),
                reply_to_message_id=message.id,
            )
    except Exception:
        pass


@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    member = await client.get_chat_member(Config.CHANNELS, message.from_user.id)
    try:
        if Config.PRIVATE is True and message.chat.username not in Config.USERNAMES:
            await message.reply_text(Translator().translate(f"Hi {message.chat.first_name} you are not allowed to use this bot!", dest=Config.LANG).text, quote=True)

        if member.status not in ["creator", "administrator", "member"]:
            
            await message.reply_text("You must be a member of the specified channel to use this bot. Please join the channel and try again.")
        else:
            await message.reply_text(
                text=script.ABOUT_MSG,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(Translator().translate('🖲️HELP🖲️', dest=Config.LANG).text, callback_data="help_data"),
                            InlineKeyboardButton(Translator().translate('✴️START✴️', dest=Config.LANG).text, callback_data="start_data"),
                        ],
                        [
                            InlineKeyboardButton(
                                Translator().translate('🏆TRUMBOTS🏆', dest=Config.LANG).text,
                                url="https://t.me/movie_time_botonly",
                            )
                        ],
                    ]
                ),
                reply_to_message_id=message.id,
            )
    except Exception:
        pass
