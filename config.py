
import os

# ==========================
# Telegram
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==========================
# APIs
# ==========================

SILVER_API = "https://api.metals.live/v1/spot/silver"

# ==========================
# تحلیل
# ==========================

# ضریب ارزش منصفانه بازار ایران
MARKET_PREMIUM = 3.2

# محدوده‌های تصمیم
BUY_LIMIT = -10
NORMAL_LIMIT = 15

# ==========================
# زمان‌بندی
# ==========================

REPORT_HOUR = 12
REPORT_MINUTE = 0

# ==========================
# منابع قیمت
# ==========================

PRICE_SOURCES = [
    "https://www.tgju.org/profile/silver_999",
    "https://tajnoghreh.com/silver-price/"
]
