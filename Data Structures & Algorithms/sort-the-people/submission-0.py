class Solution(object):
    def sortPeople(self, names, heights):
        people = list(zip(names, heights))
        people.sort(key=lambda person: person[1], reverse=True)

        res = []
        for person in people:
            res.append(person[0])

        return res