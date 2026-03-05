# (c) @PredatorHackerzZ

import asyncio
from sample_config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, cmd: Message):
    try:
        if not Config.UPDATES_CHANNEL:
            return 200
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Son, You are Banned to use me. Contact my [Support Group](https://t.me/TeleRoid14).",
                parse_mode=pyrogram.enums.ParseMode.MARKDOWN,
                link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True)
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url="https://t.me/TeleRoidGroup")
                    ]
                ]
            ),
            parse_mode=pyrogram.enums.ParseMode.MARKDOWN
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/TeleRoid14).",
            parse_mode=pyrogram.enums.ParseMode.MARKDOWN,
            link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True)
        )
        return 400
    return 200
