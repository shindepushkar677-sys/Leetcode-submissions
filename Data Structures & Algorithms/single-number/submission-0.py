class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sample = 0 
        for n in nums:
            sample = n ^ sample
        return
        