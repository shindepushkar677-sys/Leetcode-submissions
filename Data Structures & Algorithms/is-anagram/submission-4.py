class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        counts2 = {}
        if len(s) != len(t):
            return False
        for x in str(s):
            counts1[x] = counts1.get(x, 0) +1

        for x in str(t):
            counts2[x] = counts2.get(x, 0) +1

        return counts1 == counts2
        