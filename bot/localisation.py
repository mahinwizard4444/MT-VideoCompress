#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "ＨＥＹ ʙɪᴛᴄʜ  How are You!!, \n\n𝐌𝐘  𝐎𝐖𝐍𝐄𝐑 & 𝐁𝐎𝐒𝐒 [ @Jackbro007 ]﻿. \n\n<b> 😌 Ｙａａａ　Ｈｏｏｏｏｏ 💥 𝙄 𝙖𝙢 𝘼 𝘽𝙞𝙜 𝙁𝙞𝙡𝙚 𝘾𝙤𝙢𝙥𝙧𝙚𝙨𝙨 𝘽𝙤𝙩 𝙇𝙞𝙠𝙚 8️⃣𝙂𝘽 </b> \n\n/help for more details. \n\nMovies Group: @onlymovie76"

    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 Downloading... 📥 \n"
    
    UPLOAD_START = "📤 Uploading... 📤 \n"
    
    COMPRESS_START = "📀 Trying to compress... 📀"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "📥 Downloaded in {}\n\n📀 Compressed in {}\n\n📤 Uploaded in {}\n\nBy @mhd_thanzeer"

    COMPRESS_PROGRESS = "⏰ 𝐄𝐬𝐭𝐢𝐦𝐚𝐭𝐢𝐨𝐧: {}\n🚀 Progress: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    
    SAVED_RECVD_DOC_FILE = "✅ Downloaded Successfully."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot \n\n1. Send me your telegram big video file \n2. Reply to the file with: `/compress 50` \n\n [JACK](https://t.me/Jackbro007)."
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
