from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation:
    START_TEXT = """
Hi {} 👋

<b>HadiPlay Uploader میں خوش آمدید!</b>
لنک بھیجیں، پھر میں آپ سے کیپشن مانگوں گا۔
"""

    HELP_TEXT = """
1️⃣ لنک بھیجیں۔
2️⃣ بوٹ آپ سے کیپشن مانگے گا، وہ ٹائپ کریں۔
3️⃣ ویڈیو فل سائز میں اپلوڈ ہو جائے گی۔
"""

    # پروگریس بار کی مکمل تفصیل کے ساتھ
    PROGRESS = """
📊 <b>Uploading Status:</b> {0}%
🚀 <b>Speed:</b> {3}/s
✅ <b>Done:</b> {1}
🎥 <b>Total:</b> {2}
⏳ <b>ETA:</b> {4}
"""

    # یہ وہ بٹن ہیں جو ہر ویڈیو کے نیچے اپلوڈ کے بعد نظر آئیں گے
    CAPTION_BUTTONS = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🌐 Visit HadiPlay.xyz", url="https://HadiPlay.xyz")],
            [InlineKeyboardButton("📢 WhatsApp Channel", url="https://whatsapp.com/channel/0029Vb7CiqG0rGiI6HUgSB3V")]
        ]
    )

    DOWNLOAD_START = "📥 <b>ڈاؤن لوڈنگ شروع:</b>\n\n<i>{}</i>"
    UPLOAD_START = "📤 <b>ڈاؤن لوڈ مکمل! اب فل سائز ویڈیو اپلوڈ ہو رہی ہے...</b>"
    
    # یہ حصہ خالی رکھیں تاکہ آپ کا ٹائپ کیا ہوا کیپشن استعمال ہو
    CUSTOM_CAPTION_UL_FILE = "{}" 

    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "✅ <b>Success!</b>\n\nآپ کی ویڈیو فل سائز میں اپلوڈ کر دی گئی ہے۔"
