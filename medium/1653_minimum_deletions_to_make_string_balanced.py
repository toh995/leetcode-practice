class Solution:
    def minimumDeletions(self, s: str) -> int:
        if s == "":
            return 0

        b_counts = []
        b_count = 0

        for char in s:
            b_counts.append(b_count)
            if char == "b":
                b_count += 1

        # loop through the string backwards now
        ret = float("inf")
        a_count = 0

        for i in range(len(s)-1, -1 , -1):
            ret = min(ret, b_counts[i] + a_count)

            if s[i] == "a":
                a_count += 1

        return ret
