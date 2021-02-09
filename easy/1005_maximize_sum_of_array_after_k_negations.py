class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()

        maximum = float("-inf")

        for i in range(K, -1, -2):
            curr_sum = self.calculate_sum(A, i)

            if curr_sum > maximum:
                maximum = curr_sum

        return maximum

    def calculate_sum(self, A: list[int], K: int) -> List[int]:
        """
        invert the K smallest elements of A and return the sum.
        assume that A is already sorted when fed into the function
        """
        ret = 0

        for i in range(len(A)):
            if i < K:
                ret += (-A[i])
            else:
                ret += A[i]

        return ret
