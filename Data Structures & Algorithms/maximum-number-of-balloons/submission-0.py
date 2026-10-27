class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {}

        for x in text:
            counts[x] = counts.get(x, 0) + 1

        b = counts.get('b', 0)
        a = counts.get('a', 0)
        l = counts.get('l', 0) // 2
        o = counts.get('o', 0) // 2
        n = counts.get('n', 0)

        return min(b, a, l, o, n)