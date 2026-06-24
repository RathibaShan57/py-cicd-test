"""String utility functions."""


def reverse(s: str) -> str:
    return s[::-1]


def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_count(s: str) -> int:
    if not s.strip():
        return 0
    return len(s.split())


def capitalize_words(s: str) -> str:
    return " ".join(word.capitalize() for word in s.split())


def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if len(s) <= max_length:
        return s
    return s[:max_length] + suffix


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def remove_duplicates(s: str) -> str:
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)
