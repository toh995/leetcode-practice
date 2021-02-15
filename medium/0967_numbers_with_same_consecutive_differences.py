class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if k == 0:
            ret = []
            for i in range(1, 10):
                to_add = int(str(i) * n)
                ret.append(to_add)
            return ret


        @cache
        def generate_subsequences(last_digit: int, sub_length) -> List[str]:
            if sub_length == 0:
                return [""]

            next_digits = []

            if last_digit + k < 10:
                next_digits.append(last_digit+k)
            if last_digit - k >= 0:
                next_digits.append(last_digit-k)

            ret = []
            for next_digit in next_digits:
                sub_subsequences = generate_subsequences(next_digit, sub_length-1)
                ret += [str(next_digit) + s for s in sub_subsequences]
            return ret

        start_digits = [d for d in range(1, 10) if (d >= k) or (d <= 9-k)]
        ret = []

        for start_digit in start_digits:
            sub_sequences = generate_subsequences(start_digit, n-1)
            ret += [str(start_digit) + s for s in sub_sequences]

        return [int(x) for x in ret]
