from pyrogram import Client, filters
from database.database import Database # آپ کے بوٹ کی پرانی ڈیٹا بیس فائل کا حوالہ
from config import Config

# یہاں ہم فرض کر رہے ہیں کہ آپ کے ڈیٹا بیس میں کیپشن سیٹ کرنے کا فنکشن ہے
@Client.on_message(filters.private & filters.text & filters.reply)
async def set_caption(bot, message):
    if "set_caption" in message.reply_to_message.text:
        # یہاں آپ کا کیپشن ڈیٹا بیس میں سیو ہو جائے گا
        user_id = message.from_user.id
        caption_text = message.text
        # database logic here...
        await message.reply_text(f"✅ **آپ کا کیپشن سیو ہو گیا ہے!**\n\n`{caption_text}`")
