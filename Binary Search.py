class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            guess = nums[mid]

            if guess == target:
                return mid
            if guess > target: 
                r = mid - 1
            else:
                l = mid + 1
        return -1
