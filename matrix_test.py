import pytest
import matrix

def test_case_one():
    m_input = [[0,0,0],
               [0,1,0],
               [0,0,0]]

    m_output = [[0,0,0], 
                [0,1,0], 
                [0,0,0]]

    assert matrix.Solution().update_matrix(m_input) == m_output

def test_case_two():
    m_input = [[0,0,0],
               [0,1,0],
               [1,1,1]]

    m_output = [[0,0,0], 
                [0,1,0], 
                [1,2,1]]

    assert matrix.Solution().update_matrix(m_input) == m_output
