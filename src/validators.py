"""Input validation utilities."""
import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    cleaned = re.sub(r"[\s\-\(\)]", "", phone)
    return bool(re.match(r"^\+?\d{7,15}$", cleaned))


def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    return all([has_upper, has_lower, has_digit, has_special])


def is_valid_url(url: str) -> bool:
    pattern = r"^(https?://)[\w\-]+(\.[\w\-]+)+([\w\-\._~:/?#\[\]@!$&'()*+,;=%]*)$"
    return bool(re.match(pattern, url))


def is_valid_date(date_str: str) -> bool:
    pattern = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
    return bool(re.match(pattern, date_str))


def is_positive_integer(value) -> bool:
    try:
        return int(value) > 0
    except (ValueError, TypeError):
        return False


def clamp(value: float, min_val: float, max_val: float) -> float:
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val")
    return max(min_val, min(max_val, value))
