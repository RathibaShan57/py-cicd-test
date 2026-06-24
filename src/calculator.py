"""Simple calculator module."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exp: int) -> float:
    return base ** exp


def is_even(n: int) -> bool:
    return n % 2 == 0


def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b
