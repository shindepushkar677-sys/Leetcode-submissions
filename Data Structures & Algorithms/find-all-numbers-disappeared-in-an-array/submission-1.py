class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        res = []
        print(len(nums))
        for x in range(1, n+1):
            if x not in nums:
                res.append(x)
        return res
        