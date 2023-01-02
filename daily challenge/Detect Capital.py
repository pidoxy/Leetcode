# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        hash = {}
        i = 0
        count = 0

        while i < len(word):
            hash[i] = word[i].isupper()
            i += 1
        print(hash)

        caps = [value for value in hash.values()] 
        print(caps)

        for j in caps:
            if j:
                count +=1

        if count == len(word):
            return True
        if count == 1 and caps[0]:
            return True
        if count == 0 and not caps[0]:
            return True
        return False
