class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        res = []
        for x in arr:
            counts[x] = counts.get(x, 0) +1

        for x in counts:
            if counts[x] == x:
                res.append(x)  

        return max(res) if res else -1