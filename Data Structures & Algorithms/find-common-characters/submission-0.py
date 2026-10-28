class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        for x in words[0]:
            common[x] = common.get(x, 0) +1

        for word in words[1:]:
            counts = {}
            for x in word:
                counts[x] = counts.get(x, 0) +1


            for x in common:
                common[x] = min(common[x], counts.get(x, 0))

        res = []
        for x, freq in common.items():

             res.extend([x] * freq)

        return res