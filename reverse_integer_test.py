import pytest
import reverse_integer

def test_reverse():
    assert reverse_integer.Solution().reverse(123456789) == 987654321

def test_reverse_negative():
    assert reverse_integer.Solution().reverse(-123) == -321

def test_reverse_trim_zeros():
    assert reverse_integer.Solution().reverse(120) == 21

def test_reverse_overflow():
    assert reverse_integer.Solution().reverse(1534236469) == 0
