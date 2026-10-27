class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for x in details:
            x = x[11] + x[12]
            if int(x) > 60:
                count += 1
        return count
        