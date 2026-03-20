from datetime import datetime, timezone
from config import MSK_OFFSET

def get_msk_date_str() -> str:
    utc_now = datetime.now(timezone.utc)
    msk_now = utc_now + MSK_OFFSET
    return msk_now.strftime("%d.%m.%Y")

def get_report_info():
    utc_now = datetime.now(timezone.utc)
    msk_now = utc_now + MSK_OFFSET
    hour = msk_now.hour

    if 18 <= hour or hour < 6:
        base = "Отчет на 20:00"
        period = "08:00 - 20:00"
    else:
        base = "Отчет на 8:00"
        period = "20:00 - 08:00"

    text = (
        f"Уважаемый Марат Шамилевич!\n"
        f"Направляю рейтинг по выходу техники, водителей, дорожных рабочих, "
        f"очистке и обработке а/д за период с {period}."
    )
    return base, text