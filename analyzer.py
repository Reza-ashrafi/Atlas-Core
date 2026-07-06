from config import MARKET_PREMIUM, BUY_LIMIT, NORMAL_LIMIT
from sources import get_silver_spot, get_market_price


OZ_TO_GRAM = 31.1035


# =========================
# ارزش ذاتی نقره (1kg)
# =========================
def intrinsic_value(spot_price, usd_rate):
    return (1000 / OZ_TO_GRAM) * spot_price * usd_rate


# =========================
# تحلیل کامل بازار
# =========================
def analyze():

    silver = get_silver_spot()
    market = get_market_price()

    # نرخ دلار ساده (فعلاً از TGJU جدا نکردیم برای پایداری)
    # اگر خواستی بعداً جداش می‌کنیم
    import requests
    try:
        usd_data = requests.get(
            "https://api.exchangerate.host/latest?base=USD&symbols=IRR"
        ).json()
        usd = usd_data["rates"]["IRR"] / 10
    except:
        usd = 60000  # fallback

    if not silver or not market:
        return {
            "error": "data_not_available"
        }

    intrinsic = intrinsic_value(silver, usd)

    # =========================
    # ارزش منصفانه بازار ایران
    # =========================
    fair_value = intrinsic * MARKET_PREMIUM

    bubble = ((market - fair_value) / fair_value) * 100

    # =========================
    # امتیاز خرید (0 تا 100)
    # =========================
    score = 100

    # هر چی حباب بیشتر → امتیاز کمتر
    if bubble > 0:
        score -= bubble * 2

    # محدودسازی
    if score < 0:
        score = 0
    if score > 100:
        score = 100

    # =========================
    # تصمیم نهایی
    # =========================
    if bubble < BUY_LIMIT:
        decision = "🟢 فرصت خرید خوب"
    elif bubble < NORMAL_LIMIT:
        decision = "🟡 نرمال / بررسی بیشتر"
    else:
        decision = "🔴 پرریسک / حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "market": market,
        "intrinsic": intrinsic,
        "fair_value": fair_value,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }
