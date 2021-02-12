class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.reverse()
        arr2.reverse()

        if len(arr1) <= len(arr2):
            short = arr1
            long = arr2
        else:
            short = arr2
            long = arr1

        for i in range(len(short)):
            long[i] += short[i]

        i = 0
        while i < len(long):
            if long[i] in (-1, 2, 3):
                next_val: int

                if long[i] == -1:
                    next_val = 1
                    long[i] = 1

                elif long[i] == 2:
                    next_val = -1
                    long[i] = 0

                elif long[i] == 3:
                    next_val = -1
                    long[i] = 1

                if i == len(long) - 1:
                    long.append(next_val)
                else:
                    long[i+1] += next_val

            i += 1

        # remove trailing 0s
        for i in range(len(long)-1, 0, -1):
            if long[i] != 0:
                break
            else:
                long.pop()

        long.reverse()

        return long
