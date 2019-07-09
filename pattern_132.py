from typing import List

class Solution:
    def find_132_pattern(self, ints: List[int]) -> bool:
        if len(ints) < 3:
            return False
        visited = [ints[0]]

        for i in range(1, len(ints)):
            if len(visited) == 1:
                if ints[i] > visited[0]:
                    visited.append(ints[i])
                else:
                    visited[0] = ints[i]
            if len(visited) == 2:
                if ints[i] > visited[0] and ints[i] < visited[1]:
                    return True
                elif ints[i] > visited[1]:
                    visited[1] = ints[i]
                else:
                    for j in range(0,i):
                        if ints[i] > ints[j] and ints[j] < visited[0]:
                            visited = [ints[j], ints[i]]

        return False
