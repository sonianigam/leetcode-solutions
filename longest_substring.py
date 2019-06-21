class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        visited = []
        global_max = 0
        local_max = 0

        for l in s:
            if l in visited:
                global_max = max(local_max, global_max)
                visited = [l]
                local_max = 1
            else:
                visited.append(l)
                local_max+= 1

        return global_max
