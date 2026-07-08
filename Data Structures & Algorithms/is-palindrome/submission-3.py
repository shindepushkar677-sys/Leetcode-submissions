class Solution:
    def isPalindrome(self, s: str) -> bool:
        sample = ""

        for c in s:
            if c.isalnum():
                sample += c.lower()

        return sample == sample[::-1]
