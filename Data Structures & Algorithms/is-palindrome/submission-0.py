class Solution:
    def isPalindrome(self, s: str) -> bool:
        NewStr = ""
        for c in s:
            if c.isalnum():
                 s += c.lower()
        return NewStr == NewStr[::-1]
