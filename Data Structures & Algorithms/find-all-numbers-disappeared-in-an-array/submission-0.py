class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        for x in range(1, n+1):
            if x not in nums:
                res.append(x)
        return res
        