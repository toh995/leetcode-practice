class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_index = 0
        odd_index = 1
        ret = [0] * len(A)

        for num in A:
            if num % 2 == 0:
                ret[even_index] = num
                even_index += 2
            else:
                ret[odd_index] = num
                odd_index += 2

        return ret
