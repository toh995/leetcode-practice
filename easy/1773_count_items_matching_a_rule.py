class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key_dict = {
            "type": 0,
            "color": 1,
            "name": 2,
        }

        index = key_dict[ruleKey]

        return sum(
            int(item[index] == ruleValue) for item in items
        )
