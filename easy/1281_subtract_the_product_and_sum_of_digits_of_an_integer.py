from functools import reduce
import math

class Solution:
    # solution #1
    def subtractProductAndSum1(self, n: int) -> int:
        digits = list(str(n))
        digits = [int(x) for x in digits]
        product_val = reduce(lambda x,y: x*y, digits)
        sum_val = reduce(lambda x,y: x+y, digits)

        return product_val - sum_val


    # solution #2
    def subtractProductAndSum2(self, n: int) -> int:
        product_val = 1
        sum_val = 0

        for char in str(n):
            digit = int(char)

            product_val *= digit
            sum_val += digit

        return product_val - sum_val


    # solution #3
    def subtractProductAndSum3(self, n: int) -> int:
        while True:
            remainder = n % 10

            product_val *= remainder
            sum_val += remainder

            n = math.floor(n/10)

            if n == 0:
                break

        return product_val - sum_val
