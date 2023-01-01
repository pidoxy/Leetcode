
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

# Example 1:

# Input: s = "leetcode"
# Output: 0



class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = defaultdict(list)
        for i in s:
            if hash[i]:
                hash[i] += 1
            else:
                hash[i] = 1
        # print(hash)
        # for key, value in hash.items():
        #     # print(key, value)
        #     # print(s.index(key))
        #     if value == 1:
        #         print(key)
        #         print(s.index(key))
        #         return s.index(key)
        #     else:
        #         print(-1)
        #         return -1
        #     # return 0
        if 1 in [value for value in hash.values() ]:
            for j in hash:
                if hash[j] == 1:
                    return s.index(j)
                    break
        else:
            return -1
