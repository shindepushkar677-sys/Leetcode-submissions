class Solution:
    def climbStairs(self, n: int) -> int:
        ok, tokay = 1, 1

        for i in range(n -1):
            temp = ok
            ok = ok + tokay
            tokay = temp
        
        return ok