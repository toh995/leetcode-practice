class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # find the endpoints
        start_exp, start_digit = self.find_exp_digit(low)
        end_exp, end_digit = self.find_exp_digit(high)

        # iterate and build ret
        ret = []
        exp, digit = start_exp, start_digit

        while True:
            # perform digit/exp validation
            if digit >= (10 - exp):
                exp += 1
                digit = 1

            # check if we reached stopping point
            if (exp > end_exp) or (exp == end_exp and digit > end_digit):
                break

            # build number and append
            new_num = self.build_number(exp, digit)

            if low <= new_num <= high:
                ret.append(new_num)

            # increase digit for next iteration
            digit += 1

        return ret



    def find_exp_digit(self, num: int) -> Tuple[int, int]:
        exp = log(num, 10)
        exp = floor(exp)

        digit = num // (10**exp)

        if digit == 10:
            digit = 1
            exp += 1

        return exp, digit


    def build_number(self, exponent: int, digit: int) -> int:
        ret = 0

        for k in range(exponent, -1, -1):
            ret += digit * (10**k)
            digit += 1

        return ret
