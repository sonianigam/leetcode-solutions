class Solution:
    def find_median(self, nums1: int, nums2: int) -> int:
        total_length = len(nums1) + len(nums2)
        total_list = nums1 + nums2
        #need to adjust this to be O(log(m+n))
        sorted_list = sorted(total_list)
        index = int((len(nums1) + len(nums2))/2)

        if total_length % 2 != 0:
            median = sorted_list[index]
        else:
            median = (sorted_list[index-1] + sorted_list[index])/2

        return median
