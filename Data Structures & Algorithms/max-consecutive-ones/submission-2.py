class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        most = 0

        for x in nums:
            if x == 1:
                count += 1
                most = max(most, count)
            else:
                count = 0

        return most