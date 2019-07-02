import pytest
import zigzag

def test_example_one():
    s = "PAYPALISHIRING"
    num_rows = 3

    assert(zigzag.Solution().output_zigzag(s, num_rows) == "PAHNAPLSIIGYIR")

def test_example_two():
    s = "PAYPALISHIRING"
    num_rows = 4

    assert(zigzag.Solution().output_zigzag(s, num_rows) == "PINALSIGYAHRPI")
