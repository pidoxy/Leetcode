class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non alpha numeric characters and join strings
        # join empty spaces together - filter in only alpha numeric characters
        string = ''.join(filter(str.isalnum, s))
        reversedString = ""

        # reverse string in O(n) time
        for i in string:
            reversedString = i + reversedString
        print(reversedString.lower());
        print(string.lower())
        # Check reversed string against originak string
        return string.lower() == reversedString.lower()
        
