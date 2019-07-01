import numpy

class Solution:
    def two_sum(self, nums: list, target: int) -> list:
        nums_dict = dict()

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in nums_dict.keys():
                return [min(i, nums_dict[complement]), max(i, nums_dict[complement])]
            else:
                nums_dict[nums[i]] = i
