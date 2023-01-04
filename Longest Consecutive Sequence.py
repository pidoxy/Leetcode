class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
    # O(nlogn)
        nums = sorted(set(nums))
        print(nums)
        length = 1
        result = []
        i = 0

        if len(nums) == 0: 
            return 0
        while i < len(nums)-1:
            # print(nums[i])
            # i += 1
            if nums[i]+1 == nums[i+1]:
                length += 1
            else:
                result.append(length)
                length = 1
            i +=1
        result.append(length)
        print(result)
        return max(result)
        
        
               '''
        sort numbers
        get rid of duplicates using a set or hashtable
        if list is empty return 0
        '''
#         O(nlogn)
#         if not nums: return 0
#         nums = sorted(list(set(nums)))
        
        
#         sofar, output = 1,1
        
#         for i in range(1, len(nums)):
#             if nums[i-1]+1==nums[i]:
#                 sofar+=1
#             else:
#                 sofar = 1
#             output = max(output, sofar)
#         return output

#          O(n)
        nums = set(nums)
        output = 0
        
        for n in nums:
            if n-1 not in nums:
                start = n
                while start in nums:
                    start+=1
                output = max(output, start-n)
        return output


