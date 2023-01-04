class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s))
        reversedString = ""
        for i in string:
            reversedString = i + reversedString
        print(reversedString.lower());
        print(string.lower())
        return string.lower() == reversedString.lower()
        
