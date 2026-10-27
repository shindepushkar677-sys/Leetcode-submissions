class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        most = 0
        counts = {}
        for x in nums:
 
            counts[x] = counts.get(x, 0) +1

            if counts[x] > most:
                most = counts[x]
                res = x
        return res        