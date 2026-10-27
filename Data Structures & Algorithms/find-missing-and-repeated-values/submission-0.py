class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        rep = 0
        for row in grid:
            for x in row:
                if x in seen:
                    rep = x
                else:
                    seen.add(x)
        
        n = len(grid)
        miss = 0

        for x in range(1, n * n+1):
            if x not in seen:
                miss = x
                break
        return [rep, miss]
        