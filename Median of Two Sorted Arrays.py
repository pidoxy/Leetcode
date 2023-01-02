class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        median = 0

        if len(nums) % 2 != 0:
            # print((len(nums) // 2) + 1)
            median = nums[(len(nums) // 2)]
            print(median)
        else:
            median = (nums[(len(nums) // 2)] + nums[(len(nums) // 2) - 1]) / 2
            print(median)
        return median
