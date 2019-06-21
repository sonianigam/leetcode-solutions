import pytest
import longest_substring

def test_standard_substring():
    assert longest_substring.Solution().length_of_longest_substring("abcabcbb") == 3

def test_repeated_single_letter():
    assert longest_substring.Solution().length_of_longest_substring("bbbbb") == 1

def test_not_first_unique_substring():
    assert longest_substring.Solution().length_of_longest_substring("pwwkew") == 3
