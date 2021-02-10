class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = math.floor(-.5 + math.sqrt(.25 + (2*candies)))
        leftover_candies = candies - (n+1)*(n/2)

        num_rows = math.floor(n / num_people)
        extra_columns = n % num_people

        ret = []
        for i in range(num_people):
            num_candies = (num_rows * (i+1)) + (num_people * (num_rows * (num_rows-1) / 2))

            if i < extra_columns:
                num_candies += (i+1) + (num_people * (num_rows))
            elif i == extra_columns:
                num_candies += leftover_candies

            ret.append(
                int(num_candies)
            )

        return ret
