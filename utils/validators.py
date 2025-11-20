# utils/validators.py
import re

def validate_email(e):
    if not e:
        return False
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, e) is not None

def validate_phone(p):
    if not p:
        return False
    # simple phone check: digits and + allowed, length 7-15
    p2 = re.sub(r"[^\d]", "", p)
    return 7 <= len(p2) <= 15
