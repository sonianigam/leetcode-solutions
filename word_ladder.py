from typing import List
import pdb

class Node:
    def __init__(self, value, length):
        self.value = value
        self.length = length

class Solution:
    def ladder_length(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0

        start_vertex = Node(begin_word, 1)
        end_vertex = Node(end_word, 1)

        start_queue = [start_vertex]
        end_queue = [end_vertex]

        start_visited = [start_vertex.value]
        end_visited = [end_vertex.value]

        while len(start_queue) > 0 or len(end_queue) > 0:
            if len(start_queue) > 0:
                start_current = start_queue.pop(0)

                if start_current.value == end_word:
                    return start_current.length

                for w in word_list:
                    if w not in start_visited and self.neighbors(start_current.value, w):
                        print(w)
                        start_queue.append(Node(w, start_current.length + 1))
                        start_visited.append(w)

            if len(end_queue) > 0:
                end_current = end_queue.pop(0)
                print(end_current)

                if end_current.value == begin_word:
                    return end_current.length

                if end_current.value == start_current.value:
                    length = end_current.length + start_current.length
                    return length 

                for w in word_list:
                    if w not in end_visited and self.neighbors(end_current.value, w):
                        end_queue.append(Node(w, end_current.length + 1))
                        end_visited.append(w)

        return 0

    def neighbors(self, word_one, word_two):
        counter = 0

        for i in range(len(word_one)):
            if word_one[i] != word_two[i]:
                counter +=1
                if counter > 1: return False

        return True
