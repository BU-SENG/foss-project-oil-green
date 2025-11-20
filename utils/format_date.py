# utils/format_date.py
from datetime import datetime

def format_datetime(s):
    if isinstance(s, datetime):
        return s.strftime("%b %d, %Y %H:%M")
    try:
        d = datetime.fromisoformat(str(s))
        return d.strftime("%b %d, %Y %H:%M")
    except Exception:
        return str(s)
