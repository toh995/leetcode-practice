class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        ret = 0
        i, j = 0, len(people)-1

        while i < j:
            # if this is the case, then the heavy guy can't ride with a partner - has to ride alone
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1

            ret += 1

        if i == j:
            ret += 1

        return ret

