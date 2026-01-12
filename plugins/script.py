from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation:
    START_TEXT = """
Hi {} 👋

<b>میں ہادی پلے کا آفیشل اپلوڈر بوٹ ہوں۔</b>

آپ مجھے کسی بھی ویڈیو کا ڈائریکٹ لنک، یوٹیوب یا گوگل ڈرائیو کا لنک بھیجیں، میں اسے فوراً آپ کے لیے ٹیلی گرام پر اپلوڈ کر دوں گا۔
"""

    HELP_TEXT = """
<b>کیسے استعمال کریں؟</b>

1️⃣ بوٹ کو کوئی بھی ڈاؤن لوڈ لنک بھیجیں۔
2️⃣ اپنی پسند کا آپشن (Video یا File) منتخب کریں۔
3️⃣ تھوڑی دیر انتظار کریں، آپ کی فائل اپلوڈ ہو جائے گی۔

<b>ویب سائٹس:</b> HadiPlay.xyz | HadiPlay.net
"""

    ABOUT_TEXT = """
<b>♻️ بوٹ کا نام:</b> HadiPlay Uploader
<b>🌐 ویب سائٹ 1:</b> <a href="https://HadiPlay.xyz">HadiPlay.xyz</a>
<b>🌐 ویب سائٹ 2:</b> <a href="https://HadiPlay.net">HadiPlay.net</a>
<b>📑 زبان:</b> Python 3.10
<b>👲 اونر:</b> M Maaz
"""

    PROGRESS = """
🔰 اسپیڈ: {3}/s
🌀 مکمل: {1}
🎥 فائل سائز: {2}
⏳ باقی وقت: {4}
"""
    ID_TEXT = """
🆔 آپ کی ٹیلی گرام ID یہ ہے: <code>{}</code>
"""

    INFO_TEXT = """
🤹 نام: <b>{}</b>
🧑🏻‍🎓 یوزر نیم: <b>@{}</b>
🆔 ٹیلی گرام ID: <code>{}</code>
👲 اسٹیٹس: <b>HadiPlay User</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("❓ Help", callback_data="help"),
                InlineKeyboardButton("🦊 About", callback_data="about"),
            ],
            [
                InlineKeyboardButton("🌐 HadiPlay.xyz", url="https://HadiPlay.xyz"),
                InlineKeyboardButton("🌐 HadiPlay.net", url="https://HadiPlay.net"),
            ],
            [InlineKeyboardButton("📛 Close", callback_data="close")],
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠 Home", callback_data="home"),
                InlineKeyboardButton("🦊 About", callback_data="about"),
            ],
            [InlineKeyboardButton("📛 Close", callback_data="close")],
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠 Home", callback_data="home"),
                InlineKeyboardButton("❓ Help", callback_data="help"),
            ],
            [InlineKeyboardButton("📛 Close", callback_data="close")],
        ]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[InlineKeyboardButton("📛 Close", callback_data="close")]]
    )
    FORMAT_SELECTION = "اب اپنی پسند کا فارمیٹ منتخب کریں 👇"
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = "ڈاؤن لوڈنگ شروع ہو رہی ہے... ⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 ٹیلی گرام پر اپلوڈ ہو رہا ہے، براہ کرم انتظار کریں..."
    RCHD_TG_API_LIMIT = "معذرت! فائل 2GB سے بڑی ہے، جو ٹیلی گرام کی حد سے زیادہ ہے۔"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = (
        "✅ کامیابی سے اپلوڈ ہو گیا۔\n\nشکریہ HadiPlay استعمال کرنے کے لیے!"
    )
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ تھمب نیل صاف کر دیا گیا۔"
    CUSTOM_CAPTION_UL_FILE = ""
    NO_VOID_FORMAT_FOUND = "ایرر: فارمیٹ نہیں ملا <code>{}</code>"
    FREE_USER_LIMIT_Q_SZE = "ٹائم آؤٹ: سرور مصروف ہے۔"
    SLOW_URL_DECED = "یہ لنک بہت سلو ہے، براہ کرم کوئی تیز لنک ٹرائی کریں۔"
