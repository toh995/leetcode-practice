class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ret = 0

        last_char = s[0]
        start_index = 0

        for i in range(len(s)):
            if s[i] == last_char:
                continue

            else:
                sub_cost = cost[start_index : i]
                ret += (sum(sub_cost) - max(sub_cost))

                last_char = s[i]
                start_index = i

        if start_index < (len(s) - 1):
            sub_cost = cost[start_index : len(s)]
            ret += (sum(sub_cost) - max(sub_cost))

        return ret
