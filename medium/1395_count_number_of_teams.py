class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)

        # key is index in rating
        # value is another hashmap with two keys: "num_larger" and "num_smaller"
        mapping = {}
        for j in range(1, length):
            mapping[j] = {
                "num_larger": 0,
                "num_smaller": 0,
            }

            for k in range(j+1, length):
                if rating[j] < rating[k]:
                    mapping[j]["num_larger"] += 1
                else:
                    mapping[j]["num_smaller"] += 1

        counter = 0
        for i in range(length):
            for j in range(i+1, length):
                if rating[i] < rating[j]:
                    counter += mapping[j]["num_larger"]
                else:
                    counter += mapping[j]["num_smaller"]

        return counter
