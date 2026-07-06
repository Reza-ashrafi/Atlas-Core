import requests
import re
from config import SILVER_API, USER_AGENT, REQUEST_TIMEOUT

headers = {
    "User-Agent": USER_AGENT
}

# =========================
# 1. نقره جهانی (دلار)
# =========================
def get_silver_spot():
    try:
        r = requests.get(SILVER_API, timeout=REQUEST_TIMEOUT)
        data = r.json()
        return float(data[0]["price"])
    except:
        return None


# =========================
# 2. استخراج عدد از HTML
# =========================
def extract_price(html):
    numbers = re.findall(r"\d[\d,]{6,}", html)
    prices = []

    for n in numbers:
        try:
            prices.append(int(n.replace(",", "")))
        except:
            pass

    return prices


# =========================
# 3. TGJU
# =========================
def get_tgju_price():
    try:
        url = "https://www.tgju.org/profile/silver_999"
        r = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

        prices = extract_price(r.text)

        if not prices:
            return None

        return max(prices)  # معمولاً عدد بزرگ‌تر قیمت اصلی است

    except:
        return None


# =========================
# 4. تاج نقره
# =========================
def get_taj_price():
    try:
        url = "https://tajnoghreh.com/silver-price/"
        r = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

        prices = extract_price(r.text)

        if not prices:
            return None

        return max(prices)

    except:
        return None


# =========================
# 5. قیمت بازار نهایی
# =========================
def get_market_price():
    prices = []

    tgju = get_tgju_price()
    taj = get_taj_price()

    if tgju:
        prices.append(tgju)

    if taj:
        prices.append(taj)

    if not prices:
        return None

    return sum(prices) / len(prices)


# =========================
# تست سریع (اختیاری)
# =========================
if __name__ == "__main__":
    print("Silver Spot:", get_silver_spot())
    print("Market Price:", get_market_price())
