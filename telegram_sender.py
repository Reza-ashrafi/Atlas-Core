import telegram
from config import BOT_TOKEN, CHAT_ID
from analyzer import analyze

bot = telegram.Bot(token=BOT_TOKEN)


# =========================
# ساخت پیام حرفه‌ای
# =========================
def build_message(data):

    if "error" in data:
        return "❌ داده‌ها در دسترس نیستند، لطفاً بعداً دوباره تلاش کن."

    msg = f"""
📊 گزارش روزانه نقره

🌍 قیمت جهانی: {data['silver']:.2f} $
💵 دلار: {int(data['usd']):,} تومان

📦 ارزش ذاتی: {int(data['intrinsic']):,}
⚖️ ارزش منصفانه بازار: {int(data['fair_value']):,}

🏪 قیمت بازار: {int(data['market']):,}

📈 حباب: {data['bubble']:.2f}%

⭐ امتیاز خرید: {data['score']:.0f} / 100

{data['decision']}
"""

    return msg


# =========================
# ارسال پیام
# =========================
def send_report():
    data = analyze()
    message = build_message(data)

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )


# تست مستقیم
if __name__ == "__main__":
    send_report()
