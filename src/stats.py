"""Basic statistical functions."""
from typing import List


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute mean of empty list")
    return sum(values) / len(values)


def median(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute median of empty list")
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return float(sorted_vals[mid])


def mode(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute mode of empty list")
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    return max(freq, key=lambda k: freq[k])


def variance(values: List[float]) -> float:
    if len(values) < 2:
        raise ValueError("Variance requires at least 2 values")
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / (len(values) - 1)


def std_dev(values: List[float]) -> float:
    return variance(values) ** 0.5


def data_range(values: List[float]) -> float:
    if not values:
        raise ValueError("Cannot compute range of empty list")
    return max(values) - min(values)


def percentile(values: List[float], p: float) -> float:
    if not values:
        raise ValueError("Cannot compute percentile of empty list")
    if not 0 <= p <= 100:
        raise ValueError("Percentile must be between 0 and 100")
    sorted_vals = sorted(values)
    index = (p / 100) * (len(sorted_vals) - 1)
    lower = int(index)
    upper = lower + 1
    if upper >= len(sorted_vals):
        return float(sorted_vals[-1])
    return sorted_vals[lower] + (index - lower) * (sorted_vals[upper] - sorted_vals[lower])
