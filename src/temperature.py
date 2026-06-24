"""Temperature conversion utilities."""


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    if c < -273.15:
        raise ValueError("Temperature below absolute zero")
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    if k < 0:
        raise ValueError("Kelvin cannot be negative")
    return k - 273.15


def fahrenheit_to_kelvin(f: float) -> float:
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float) -> float:
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def describe_temperature(c: float) -> str:
    if c < 0:
        return "freezing"
    elif c < 15:
        return "cold"
    elif c < 25:
        return "comfortable"
    elif c < 35:
        return "warm"
    else:
        return "hot"
