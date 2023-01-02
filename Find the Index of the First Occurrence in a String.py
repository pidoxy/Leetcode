class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == "":
        #     return 0;
        # else:
        if needle not in haystack:
            return -1
        else:
            print(haystack.index(needle))
            return haystack.index(needle)
