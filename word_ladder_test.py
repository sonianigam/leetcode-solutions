import word_ladder
import pytest

def test_standard_transformations():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 5

def test_end_word_not_word_list():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 0

def test_are_neighbors_happy():
    w1 = "hit"
    w2 = "hot"

    assert word_ladder.Solution().neighbors(w1, w2) == True

def test_are_neighbors_sad():
    w1 = "pit"
    w2 = "lot"

    assert word_ladder.Solution().neighbors(w1, w2) == False
