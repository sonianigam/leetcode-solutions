from typing import List
from collections import deque, defaultdict

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

        start_queue = deque([start_vertex])
        end_queue = deque([end_vertex])

        start_visited = {start_vertex.value: start_vertex.length}
        end_visited = {end_vertex.value: end_vertex.length}

        neighbors_dict = self.neighbors(word_list, len(begin_word))

        while len(start_queue) > 0 and len(end_queue) > 0:
            if len(start_queue) > 0:
                start_current = start_queue.popleft()

                if start_current.value == end_word:
                    return start_current.length

                if start_current.value in end_visited.keys():
                    length = start_current.length + end_visited[start_current.value] - 1
                    return length

                s_current_neighbors = []

                for i in range(len(start_current.value)):
                    key = start_current.value[:i] + "*" + start_current.value[i+1:]
                    s_current_neighbors.extend(neighbors_dict[key])

                for w in s_current_neighbors:
                    if w not in start_visited.keys():
                        if w == end_word:
                            return start_current.length + 1
                        node = Node(w, start_current.length + 1)
                        start_queue.append(node)
                        start_visited[node.value] = node.length

            if len(end_queue) > 0:
                end_current = end_queue.popleft()

                if end_current.value == begin_word:
                    return end_current.length

                if end_current.value in start_visited.keys():
                    length = end_current.length + start_visited[end_current.value] - 1
                    return length

                e_current_neighbors = []

                for i in range(len(end_current.value)):
                    key = end_current.value[:i] + "*" + end_current.value[i+1:]
                    e_current_neighbors.extend(neighbors_dict[key])

                for w in e_current_neighbors:
                    if w not in end_visited.keys():
                        if w == begin_word:
                            return end_current.length + 1
                        node = Node(w, end_current.length + 1)
                        end_queue.append(node)
                        end_visited[node.value] = node.length

        return 0

    def neighbors(self, word_list, num):
        d = defaultdict(list)

        for w in word_list:
            for i in range(num):
                key = w[:i] + "*" + w[i+1:]
                d[key].append(w)

        return d
