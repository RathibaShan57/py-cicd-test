"""Tests for string_utils module."""
import pytest
from src.string_utils import (
    reverse,
    is_palindrome,
    word_count,
    capitalize_words,
    truncate,
    count_vowels,
    remove_duplicates,
)


class TestReverse:
    def test_basic(self):
        assert reverse("hello") == "olleh"

    def test_empty(self):
        assert reverse("") == ""

    def test_single_char(self):
        assert reverse("a") == "a"

    def test_palindrome_word(self):
        assert reverse("racecar") == "racecar"


class TestIsPalindrome:
    def test_true(self):
        assert is_palindrome("racecar") is True

    def test_false(self):
        assert is_palindrome("hello") is False

    def test_with_spaces(self):
        assert is_palindrome("a man a plan a canal panama") is True

    def test_mixed_case(self):
        assert is_palindrome("MadamI") is False

    def test_empty(self):
        assert is_palindrome("") is True


class TestWordCount:
    def test_sentence(self):
        assert word_count("hello world") == 2

    def test_empty(self):
        assert word_count("") == 0

    def test_whitespace_only(self):
        assert word_count("   ") == 0

    def test_single_word(self):
        assert word_count("python") == 1


class TestCapitalizeWords:
    def test_basic(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_already_capitalized(self):
        assert capitalize_words("Hello World") == "Hello World"

    def test_mixed(self):
        assert capitalize_words("the quick BROWN fox") == "The Quick Brown Fox"


class TestTruncate:
    def test_no_truncation_needed(self):
        assert truncate("hi", 10) == "hi"

    def test_exact_length(self):
        assert truncate("hello", 5) == "hello"

    def test_truncated(self):
        assert truncate("hello world", 5) == "hello..."

    def test_custom_suffix(self):
        assert truncate("hello world", 5, suffix="!") == "hello!"

    def test_zero_length(self):
        assert truncate("hello", 0) == "..."

    def test_negative_length(self):
        with pytest.raises(ValueError, match="max_length must be non-negative"):
            truncate("hello", -1)


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("hello") == 2

    def test_no_vowels(self):
        assert count_vowels("gym") == 0

    def test_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_mixed_case(self):
        assert count_vowels("Hello World") == 3


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates("aabbcc") == "abc"

    def test_no_duplicates(self):
        assert remove_duplicates("abc") == "abc"

    def test_empty(self):
        assert remove_duplicates("") == ""

    def test_preserves_order(self):
        assert remove_duplicates("banana") == "ban"
