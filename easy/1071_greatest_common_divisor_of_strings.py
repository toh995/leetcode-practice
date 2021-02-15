class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find divisors of len(str1) and len(str2)
        divisors1 = self.find_divisors(len(str1))
        divisors2 = self.find_divisors(len(str2))

        t_lengths = divisors1 & divisors2

        max_length = 0
        for t_length in t_lengths:
            t = str1[:t_length]

            # check if t divides both strings
            divides_str1 = (str1 == t * (len(str1)//t_length))
            divides_str2 = (str2 == t * (len(str2)//t_length))

            if divides_str1 and divides_str2:
                max_length = max(max_length, t_length)

        return str1[:max_length]


    def find_divisors(self, num: int) -> Set[int]:
        divisors = set([1, num])

        for k in range(2, (num//2) + 1):
            if num % k == 0:
                divisors.add(k)
                divisors.add(num // k)

        return divisors
