import os
import asyncio
from youtube_dl import YoutubeDL
from pyrogram import enums, Client, filters
from pyrogram.types import Message
from config import Config
from plugins.functions.help_ytdl import get_file_extension_from_url, get_resolution

async def send_video(message, info_dict, video_file):
    basename = video_file.rsplit(".", 1)[-2]
    download_location = f"{Config.DOWNLOAD_LOCATION}/{message.from_user.id}.jpg"
    thumb = download_location if os.path.isfile(download_location) else None
    
    # Ask for Custom Caption
    ask_cap = await message.chat.ask("🎬 **ویڈیو کے لیے کیپشن ٹائپ کریں:**", timeout=60)
    caption_text = ask_cap.text if ask_cap else info_dict.get("title")

    width, height = get_resolution(info_dict)
    await message.reply_video(
        video_file,
        caption=f"{caption_text}\n\n🌐 HadiPlay.xyz",
        duration=int(float(info_dict.get("duration", 0))),
        width=width, height=height,
        supports_streaming=True, # Full Size Video
        thumb=thumb
    )
    os.remove(video_file)

@Client.on_callback_query(filters.regex("^ytdl_video$"))
async def callback_query_ytdl_video(bot, callback_query):
    url = callback_query.message.reply_to_message.text
    ydl_opts = {
        "format": "best[ext=mp4]/best", # Best Quality
        "outtmpl": "%(title)s.%(ext)s",
    }
    with YoutubeDL(ydl_opts) as ydl:
        await callback_query.edit_message_text("📥 **Downloading Best Quality...**")
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)
        await send_video(callback_query.message, info_dict, video_file)
