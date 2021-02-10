class Solution:
    def reverseVowels(self, s: str) -> str:
        # get vowel indexes
        vowel_indexes = []
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                vowel_indexes.append(i)

        ret = list(s)

        left = 0
        right = len(vowel_indexes) - 1

        while left <= right:
            left_index = vowel_indexes[left]
            right_index = vowel_indexes[right]

            temp = ret[left_index]
            ret[left_index] = ret[right_index]
            ret[right_index] = temp

            left += 1
            right -= 1

        return "".join(ret)
