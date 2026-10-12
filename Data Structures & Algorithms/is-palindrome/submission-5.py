import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x= "".join(s.split())
        x= re.sub(r'[, \- ? ! \' \" . :]', '', s)
        print(x)
        y= x.lower()
        if y[::-1] == y:
            return True
        else:
            return False