class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        differences = [
            A[i+1] - A[i] for i in range(len(A)-1)
        ]

        ret = 0

        last_difference = None
        curr_count = 1

        for curr_difference in differences:
            if curr_difference == last_difference:
                curr_count += 1

            else:
                n = curr_count - 1
                ret += int((n+1) * (n/2))

                # reset values
                last_difference = curr_difference
                curr_count = 1

        if curr_count >= 2:
            n = curr_count - 1
            ret += int((n+1) * (n/2))

        return ret
