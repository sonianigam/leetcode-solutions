class Solution:
    def reverse(self, x: int) -> int:
        num_list = [digit for digit in str(x)]

        if num_list[0] == "-":
            neg = num_list.pop(0)
            num_list.append(neg)

        num_list.reverse()
        r_num = int("".join(num_list))

        if r_num <= -2**31 or r_num >= 2**31 - 1: return 0
        return r_num
