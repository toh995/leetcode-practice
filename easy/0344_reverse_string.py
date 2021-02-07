import math

class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        half_length = math.floor(length / 2)

        for i in range(half_length):
            char1 = s[i]
            char2 = s[length-i-1]

            s[i] = char2
            s[length-i-1] = char1
