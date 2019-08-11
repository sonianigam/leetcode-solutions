import solve_equation
import pytest

solution = solve_equation.Solution()

def test_standard_case():
    assert solution.compute("x+5-3+x=6+x-2") == "x=2"

def test_zero_case():
    assert solution.compute("2x=x") == "x=0"

def test_failed_case():
    assert solution.compute("-x=-1") == "x=1"

def test_negative_case():
    assert solution.compute("2x+3x-6x=x+2") == "x=-1"

def test_no_solutions():
    assert solution.compute("x=x+2") == "No solution"

def test_infinite_solutions():
    assert solution.compute("x=x") == "Infinite solutions"
