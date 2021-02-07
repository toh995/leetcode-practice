from typing import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)

        # if no dupes, then return the length of the string
        if not self.has_dupes(s):
            return length

        max_length = 0

        for i in range(length):
            for j in range(i+1, length):
                # check if s[j] is a dupe
                if s[j] in s[i:j]:
                    new_length = j - i

                    if new_length > max_length:
                        max_length = new_length
                    break

                # check if j is the last index
                if j == length - 1:
                    new_length = j - i + 1

                    if new_length > max_length:
                        max_length = new_length
                    break

        return max_length


    def has_dupes(self, s: str) -> bool:
        seen = []

        for char in s:
            if char in seen:
                return True
            else:
                seen.append(char)

        return False
