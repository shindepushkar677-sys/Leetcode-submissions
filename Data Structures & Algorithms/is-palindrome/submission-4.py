class Solution:
    def isPalindrome(self, s: str) -> bool:
        kush = ""
        

        for c in s:
           if c.isalnum():
             kush += c.lower()
           
        return kush == kush[::-1]
        