class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)

        if num[0] == "-":
            num = num[1:] + "-"

        r_num  = int(num[::-1])

        if r_num <= -2**31 or r_num >= 2**31 - 1: return 0
        return r_num

        print(num)

