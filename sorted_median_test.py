import pytest
import sorted_median


def test_example_one():
    nums1 = [1, 3]
    nums2 = [2]
    assert(sorted_median.Solution().find_median(nums1, nums2)) == 2.0

def test_example_two():
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert(sorted_median.Solution().find_median(nums1, nums2)) == 2.5
