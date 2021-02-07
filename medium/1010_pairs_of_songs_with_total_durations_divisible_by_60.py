import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        divisor = 60

        # first map to mod 60
        remainders = [x % divisor for x in time]

        # build hash map, where key is remainder, and value is # of appearances
        frequency_map = {}
        for remainder in remainders:
            if remainder not in frequency_map:
                frequency_map[remainder] = 1
            else:
                frequency_map[remainder] += 1

        # get the remainders that are <= divisor/2
        small_remainders = frequency_map.keys()
        small_remainders = [x for x in small_remainders if x <= divisor/2]

        count = 0

        for remainder in small_remainders:
            if (remainder == 0) or (remainder == divisor/2):
                num_appearances = frequency_map[remainder]

                if num_appearances >= 2:
                    # find the number of 2-pairs we can make with num_appearances
                    factorial = math.factorial
                    num_2pairs = factorial(num_appearances) / (factorial(2) * factorial(num_appearances - 2))

                    count += num_2pairs

            else:
                other_remainder = divisor - remainder

                if other_remainder in frequency_map:
                    frequency1 = frequency_map[remainder]
                    frequency2 = frequency_map[other_remainder]

                    count += frequency1*frequency2

        return int(count)
