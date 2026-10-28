class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for x in str(s):
            counts[x] = counts.get(x, 0) +1

        for i, x in enumerate(s):
            if counts[x] == 1:
                return i
        return -1
        