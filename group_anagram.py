from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            key = hash(''.join(sorted(word)))
            anagrams[key].append(word)

        output = anagrams.values()

        return output
