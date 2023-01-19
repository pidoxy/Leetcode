class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if len(nums) == 1: return nums[0]
        l, r = 0, len(nums)-1
        min_val = nums[r]
        while l <= r:
            mid = (l+r)//2

            if nums[mid] <= min_val:
                r = mid - 1
                min_val = min(nums[mid], min_val)
                print(min_val)
            elif nums[mid] > min_val:
                l = mid + 1
        return min_val
