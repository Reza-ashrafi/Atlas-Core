def analyze():
    # دیتا موقت برای اینکه ربات نخوابه
    silver = 28.5
    usd = 60000

    intrinsic = silver * usd
    market = intrinsic * 1.02

    bubble = ((market - intrinsic) / intrinsic) * 100

    score = max(0, 100 - abs(bubble) * 10)

    decision = "📈 فعلاً پایدار - تستی"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
    }
    usd = 60000  # فعلاً ثابت برای جلوگیری از خطا

    intrinsic = silver * usd
    market = intrinsic * 1.05  # شبیه‌سازی ساده

    bubble = ((market - intrinsic) / intrinsic) * 100

    score = max(0, 100 - abs(bubble) * 10)

    decision = "📈 مناسب بررسی خرید" if bubble < 5 else "⚠️ حباب بالا"

    return {
        "silver": silver,
        "usd": usd,
        "intrinsic": intrinsic,
        "market": market,
        "bubble": bubble,
        "score": score,
        "decision": decision
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
