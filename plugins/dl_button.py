import asyncio
import os
import time
from datetime import datetime
import aiohttp
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.functions.display_progress import progress_for_pyrogram, humanbytes, TimeFormatter
from plugins.script import Translation
from plugins.utitles import Mdata01, Mdata02, Mdata03
from config import Config

async def ddl_call_back(bot, update):
    cb_data = update.data
    tg_send_type, _, youtube_dl_ext = cb_data.split("=")
    youtube_dl_url = update.message.reply_to_message.text
    
    # 1. Ask for Thumbnail
    thumb_msg = await bot.send_message(
        update.message.chat.id,
        "🖼 **مرحلہ 1: تھمب نیل منتخب کریں**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("⏩ Skip", callback_data="skip_thumb"),
             InlineKeyboardButton("🖼 Upload New", callback_data="set_thumb")]
        ])
    )
    # Note: Logic for skip/set should be in callbacks.py, for now continuing with default thumb
    thumb_path = f"{Config.DOWNLOAD_LOCATION}/{update.from_user.id}.jpg"
    thumb = thumb_path if os.path.isfile(thumb_path) else None

    # 2. Ask for Caption
    cap_msg = await bot.ask(update.message.chat.id, "✍️ **مرحلہ 2: کیپشن ٹائپ کریں یا 'auto' لکھیں:**", timeout=60)
    user_caption = update.message.reply_to_message.text if cap_msg.text.lower() == "auto" else cap_msg.text

    custom_file_name = os.path.basename(youtube_dl_url.split("?")[0])
    if f".{youtube_dl_ext}" not in custom_file_name:
        custom_file_name += f".{youtube_dl_ext}"

    download_directory = f"{Config.DOWNLOAD_LOCATION}/{update.from_user.id}/{custom_file_name}"
    if not os.path.isdir(os.path.dirname(download_directory)):
        os.makedirs(os.path.dirname(download_directory))

    await bot.edit_message_text(update.message.chat.id, update.message.id, text=Translation.DOWNLOAD_START.format(custom_file_name))

    async with aiohttp.ClientSession() as session:
        c_time = time.time()
        await download_coroutine(bot, session, youtube_dl_url, download_directory, update.message.chat.id, update.message.id, c_time)

    if os.path.exists(download_directory):
        await bot.edit_message_text(update.message.chat.id, update.message.id, text=Translation.UPLOAD_START)
        start_time = time.time()

        if tg_send_type == "video":
            width, height, duration = await Mdata01(download_directory)
            await bot.send_video(
                chat_id=update.message.chat.id,
                video=download_directory,
                thumb=thumb,
                caption=f"{user_caption}\n\n🎬 @HadiPlay",
                duration=duration, width=width, height=height,
                supports_streaming=True, # For Full Size
                progress=progress_for_pyrogram,
                progress_args=(Translation.UPLOAD_START, update.message, start_time)
            )
        else:
            await bot.send_document(
                chat_id=update.message.chat.id,
                document=download_directory,
                thumb=thumb,
                caption=f"{user_caption}\n\n🎬 @HadiPlay",
                progress=progress_for_pyrogram,
                progress_args=(Translation.UPLOAD_START, update.message, start_time)
            )
        os.remove(download_directory)
