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

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image


@pyrogram.Client.on_message(pyrogram.filters.command(["rename"]))
async def rename_doc(bot, update):
    if (" " in update.text) and (update.reply_to_message is not None):
        cmd, file_name = update.text.split(" ", 1)
        if len(file_name) > 128:
            await update.reply_text(
                Translation.IFLONG_FILE_NAME.format(
                    alimit="128",
                    num=len(file_name)
                )
            )
            return
        caption_str = ""
        caption_str += "<b>"
        caption_str += file_name
        caption_str += "</b>"
        if Config.CHANNEL_URL is not None:
            caption_str += "\n\nJoin: "
            caption_str += "<a href='"
            caption_str += f"{Config.CHANNEL_URL}"
            caption_str += "'>"
            caption_str += f"{Config.CHANNEL_URL}"
            caption_str += "</a>"
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.DOWNLOAD_START,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.reply_to_message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START,
                a,
                c_time
            )
        )
        if the_real_download_location is not None:
            try:
                await bot.edit_message_text(
                    text=Translation.SAVED_RECVD_DOC_FILE,
                    chat_id=update.chat.id,
                    message_id=a.id
                )
            except:
                pass
            if "IndianMovie" in the_real_download_location:
                await bot.edit_message_text(
                    text=Translation.RENAME_403_ERR,
                    chat_id=update.chat.id,
                    message_id=a.id
                )
                return
            new_file_name = download_location + file_name
            os.rename(the_real_download_location, new_file_name)
            # await bot.edit_message_text(
            #     text=Translation.UPLOAD_START,
            #     chat_id=update.chat.id,
            #     message_id=a.id
            # )
            logger.info(the_real_download_location)
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                logger.info('setting thumb.jpg as thumbnail')
                thumb_image_path = "thumb.jpg"
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            c_time = time.time()
            await bot.send_document(
                chat_id=update.chat.id,
                document=new_file_name,
                thumb=thumb_image_path,
                caption=caption_str,
                # reply_markup=reply_markup,
                reply_parameters=pyrogram.types.ReplyParameters(message_id=update.reply_to_message.id),
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START,
                    a, 
                    c_time
                )
            )
            try:
                os.remove(new_file_name)
                os.remove(thumb_image_path)
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=update.chat.id,
                message_id=a.id,
                link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True)
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.REPLY_TO_DOC_FOR_RENAME_FILE,
            reply_parameters=pyrogram.types.ReplyParameters(message_id=update.id)
        )
