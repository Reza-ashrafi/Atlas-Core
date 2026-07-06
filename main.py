import time
from telegram_sender import send_report


# =========================
# اجرای یک‌باره گزارش
# =========================
def run_once():
    send_report()


# =========================
# اجرای روزانه (لوکال / سرور)
# =========================
def run_daily():
    while True:
        try:
            print("📊 Running daily silver report...")
            send_report()
            print("✅ Report sent successfully")

        except Exception as e:
            print("❌ Error:", e)

        # 24 ساعت صبر
        time.sleep(86400)


# =========================
# حالت اجرا
# =========================
if __name__ == "__main__":
    run_daily()
