#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Kirodewal

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.display_progress import progress_for_pyrogram
from helper_funcs.help_Nekmo_ffmpeg import take_screen_shot, cult_small_video

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser


@pyrogram.Client.on_message(pyrogram.filters.command(["ffmpegrobot"]))
async def ffmpegrobot_ad(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.FF_MPEG_RO_BOT_AD_VER_TISE_MENT,
        link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["trim"]))
async def trim(bot, update):
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".FFMpegRoBot.mkv"
    if os.path.exists(saved_file_path):
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
        commands = update.command
        if len(commands) == 3:
            # output should be video
            cmd, start_time, end_time = commands
            o = await cult_small_video(saved_file_path, Config.DOWNLOAD_LOCATION, start_time, end_time)
            logger.info(o)
            if o is not None:
                await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.UPLOAD_START,
                    message_id=a.id
                )
                c_time = time.time()
                await bot.send_video(
                    chat_id=update.chat.id,
                    video=o,
                    # caption=description,
                    # duration=duration,
                    # width=width,
                    # height=height,
                    supports_streaming=True,
                    # reply_markup=reply_markup,
                    # thumb=thumb_image_path,
                    reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
                os.remove(o)
                await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                    link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
                    message_id=a.id
                )
        elif len(commands) == 2:
            # output should be screenshot
            cmd, start_time = commands
            o = await take_screen_shot(saved_file_path, Config.DOWNLOAD_LOCATION, start_time)
            logger.info(o)
            if o is not None:
                await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.UPLOAD_START,
                    message_id=a.id
                )
                c_time = time.time()
                await bot.send_document(
                    chat_id=update.chat.id,
                    document=o,
                    # thumb=thumb_image_path,
                    # caption=description,
                    # reply_markup=reply_markup,
                    reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
                c_time = time.time()
                await bot.send_photo(
                    chat_id=update.chat.id,
                    photo=o,
                    # caption=Translation.CUSTOM_CAPTION_UL_FILE,
                    reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id),
                    progress=progress_for_pyrogram,
                    progress_args=(
                        Translation.UPLOAD_START,
                        a,
                        c_time
                    )
                )
                os.remove(o)
                await bot.edit_message_text(
                    chat_id=update.chat.id,
                    text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                    link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
                    message_id=a.id
                )
        else:
            await bot.edit_message_text(
                chat_id=update.chat.id,
                text=Translation.FF_MPEG_RO_BOT_RE_SURRECT_ED,
                message_id=a.id
            )
    else:
        # reply help message
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FF_MPEG_RO_BOT_STEP_TWO_TO_ONE,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["storageinfo"]))
async def storage_info(bot, update):
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".FFMpegRoBot.mkv"
    if os.path.exists(saved_file_path):
        metadata = extractMetadata(createParser(saved_file_path))
        duration = None
        if metadata.has("duration"):
            duration = metadata.get('duration')
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FF_MPEG_RO_BOT_STOR_AGE_INFO.format(duration),
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
    else:
        # reply help message
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FF_MPEG_RO_BOT_STEP_TWO_TO_ONE,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )


@pyrogram.Client.on_message(pyrogram.filters.command(["clearffmpegmedia"]))
async def clear_media(bot, update):
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".FFMpegRoBot.mkv"
    if os.path.exists(saved_file_path):
        os.remove(saved_file_path)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.FF_MPEG_DEL_ETED_CUSTOM_MEDIA,
        reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
    )


@pyrogram.Client.on_message(pyrogram.filters.command(["downloadmedia"]))
async def download_media(bot, update):
    saved_file_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".FFMpegRoBot.mkv"
    if not os.path.exists(saved_file_path):
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
        try:
            c_time = time.time()
            await bot.download_media(
                message=update.reply_to_message,
                file_name=saved_file_path,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.DOWNLOAD_START,
                    a,
                    c_time
                )
            )
        except (ValueError) as e:
            await bot.edit_message_text(
                chat_id=update.chat.id,
                text=str(e),
                message_id=a.id
            )
        else:
            await bot.edit_message_text(
                chat_id=update.chat.id,
                text=Translation.SAVED_RECVD_DOC_FILE,
                message_id=a.id
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
