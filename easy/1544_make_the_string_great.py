class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s

        i = 0
        while (i < len(s) - 1):
            if s[i] == s[i+1].swapcase():
                s = s[:i] + s[i+2:]
                i = 0 if (i == 0) else i-1
                continue
            else:
                i += 1

        return s
