# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right, left = [1],[1]
        leftCount, rightCount = 1, 1

        for i in range(len(nums)-1, 0, -1):
            rightCount *= nums[i]
            right.append(rightCount)
            # print(rightCount)  
        # print(right[::-1])
        for i in range(0, len(nums)-1):
            leftCount *= nums[i]
            # print(leftCount) 
            left.append(leftCount)  
        # print(left)  
        right = right[::-1]
        for k in range(len(right)):
            right[k] *= left[k]
        return right

          
        
