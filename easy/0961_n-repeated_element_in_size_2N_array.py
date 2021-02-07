class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        seen = set()

        for val in A:
            if val in seen:
                return val
            else:
                seen.add(val)
