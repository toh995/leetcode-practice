class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        i = j = 0

        while True:

            # move i and j to the next index
            while (i < len(start)) and (start[i] == "X"):
                i += 1

            while (j < len(end)) and (end[j] == "X"):
                j += 1

            # if both i and j are out of bounds, then we have reached the end with no problems.
            # return True here.
            if (i >= len(start)) and (j >= len(end)):
                return True

            # if one of i and j are out of bounds, then one has reached the end, but the other hasn't yet.
            # return False here.
            if (i >= len(start)) or (j >= len(end)):
                return False

            # check if valid
            if start[i] != end[j]:
                return False

            if (start[i] == "L") and (i < j):
                return False

            if (start[i] == "R") and (i > j):
                return False

            # move to the next index
            i += 1
            j += 1
