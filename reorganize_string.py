from collections import OrderedDict

class Solution:
    def reorganize_string(self, s: str) -> str:
        unique = set(s)
        counts = dict()
        result = []

        for c in unique:
            if s.count(c) >= len(s)/2 + 1:
                return ""
            counts[c] = s.count(c)

        sorted_counts = OrderedDict(sorted(counts.items(), key=lambda t: t[1]), reverse=True)

        for k in sorted_counts:
            if k == "reverse":
                pass
            else:
                count = sorted_counts[k]
                result.extend(k * count)

        output = [None] * len(result)
        index = int(len(s)/2)

        output[::2] = result[index:]
        output[1::2] = result[:index]

        output = "".join(output)

        return(output)
