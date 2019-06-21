from typing import List

class Node:
    def __init__(self, value, length):
        self.value = value
        self.length = length

class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0

        vertex = Node(begin_word, 1)

        queue = [vertex]
        visited = [vertex.value]

        while len(queue) > 0:
            current = queue.pop(0)

            if current.value == end_word:
                return current.length

            for w in word_list:
                if (w not in visited) and (self.neighbors(current.value, w)):
                    queue.append(Node(w, current.length + 1))
                    visited.append(w)

        return 0



    def neighbors(self, word_one, word_two):
        counter = 0

        for i in range(len(word_one)):
            if word_one[i] != word_two[i]:
                counter +=1
                if counter > 1: return False

        return True
