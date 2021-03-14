class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {
            "a": a,
            "b": b,
            "c": c,
            "": 0,
        }

        def helper(prev_char: str) -> str:
            '''
            find the next char - this will be a string that satisfies the following conditions:
            - is NOT the prev_char
            - out of the remaining candidates, next_char has the highest count
            '''
            candidates = [char for char in counts.keys() if char != prev_char]
            highest_count = max(counts[candidate] for candidate in candidates)

            next_char: str
            for candidate in candidates:
                if couacnts[candidate] == highest_count:
                    next_char = candidate
                    break

            # if there are 0 of the next_char, then we can't append anything else - so return ""
            if counts[next_char] == 0:
                return ""

            # figure out how many times we append next_char to the string
            max_val = max(counts.values())

            if (counts[prev_char] != max_val) and (counts[next_char] >= 2):
                counts[next_char] -= 2
                return (next_char*2) + helper(next_char)

            else:
                counts[next_char] -= 1
                return next_char + helper(next_char)

        return helper("")
