import pytest
import reorganize_string

solution = reorganize_string.Solution()

def test_happy_path():
    assert solution.reorganize_string("aab") == "aba"

def test_sad_path():
    assert solution.reorganize_string("aaab") == ""
