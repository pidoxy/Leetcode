class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

#       O(n) + O(nlogn) time
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        print(nums)

        nums.sort()

        return nums
      
#       O(n) time - two pointer
        res = []

        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l]*nums[l])
                l += 1
            else:
                res.append(nums[r]*nums[r])
                r -= 1
        return res[::-1]

