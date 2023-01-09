class Solution:
    def maxArea(self, height: List[int]) -> int:

# Brute Force - Too slow - O(n^2) time
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                # print(min(height[i], height[j]))
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                res = max(res, area)
        # print(res)
        return res

      
#       O(n) time
        l,r = 0, len(height)-1
        res=0
# move l if it is the smaller height, and vice versa
        # print(l,r)
        while l != r:
            h = min(height[l], height[r])
            w = r-l
            area = h*w
            res = max(res,area)
            if height[l] > height[r]:
                r -= 1
            elif height[r] > height[l]:
                l += 1
            elif height[l+1] > height[r-1]:
                r -= 1
            else:
                l += 1
        # print(res)
        return res
