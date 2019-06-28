import word_ladder
import pytest
import test

def test_standard_transformations():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 5

def test_end_word_not_in_word_list():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 0

def test_failed_use_case():
    begin_word = "hot"
    end_word = "dog"
    word_list = ["hot","dog","dot"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 3

def test_failed_use_case_two():
    begin_word = "a"
    end_word = "c"
    word_list = ["a", "b", "c"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 2

def test_failed_use_case_two():
    begin_word = "red"
    end_word = "tax"
    word_list = ["ted","tex","red","tax","tad","den","rex","pee"]

    assert word_ladder.Solution().ladder_length(begin_word, end_word, word_list) == 4

def test_neighbors_happy():
    word_list = ["it", "is"]
    num = 2

    result = {"i*": ["it", "is"], "*t": ["it"], "*s": ["is"]}

    assert word_ladder.Solution().neighbors(word_list, num) == result
