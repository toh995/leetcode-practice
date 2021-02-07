class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case
        if not strs:
            return ""

        shortest_string = self.get_shortest_string(strs)
        ret = ""

        for i, char in enumerate(shortest_string):
            should_add = all(string[i] == char for string in strs)

            if should_add:
                ret += char
            else:
                break

        return ret


    def get_shortest_string(self, strs: List[str]) -> str:
        shortest_string = strs[0]

        for string in strs:
            if len(string) < len(shortest_string):
                shortest_string = string

        return shortest_string
