import pytest
import pattern_132

solution = pattern_132.Solution()

def test_case_one():
    i = [1,2,3,4]
    assert(solution.find_132_pattern(i) == False)

def test_case_two():
    i = [1,4,2]
    assert(solution.find_132_pattern(i) == True)

def test_case_negative():
    i = [-1,3,2,0]
    assert(solution.find_132_pattern(i) == True)

def test_case_three():
    i = [5,6,1,4,2]
    assert(solution.find_132_pattern(i) == True)
