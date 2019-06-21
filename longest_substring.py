class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        visited = []
        max_length = 0

        for l in s:
            if l in visited:
                index = visited.index(l)
                visited = visited[index+1:]

            visited.append(l)
            max_length = max(max_length, len(visited))

        return max_length
