class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (1+r) // 2
            if num[m] > target:
                r = m - 1
            elif num[m] < target:
                l = m + 1
            else:
                return m
        return -1         




        