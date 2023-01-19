class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        min_val = nums[r]
        while l <= r:
            middle = (l+r)//2

            if nums[middle] == target:
                return middle
            elif nums[l] <= nums[middle]:
                # checking for 1st half from left end to middle 
                if (nums[l] <= target and target < nums[middle]):
                    r = middle-1
                else:
                    l = middle+1
            else:
                # checking for 2nd half from middle to right end
                if (target > nums[middle] and target <= nums[r]):
                    l = middle+1
                else:
                    r = middle-1
        return -1
