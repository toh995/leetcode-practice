class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)

        left = 0
        right = len(S) - 1

        while True:
            # move the left pointer
            for _ in range(right-left):
                if S[left].isalpha():
                    break
                else:
                    left += 1

            # move the right pointer
            for _ in range(right-left):
                if S[right].isalpha():
                    break
                else:
                    right -= 1

            # check if we should break
            if left >= right:
                break

            # swap the right and left
            S[left], S[right] = S[right], S[left]

            left += 1
            right -= 1

        return "".join(S)
