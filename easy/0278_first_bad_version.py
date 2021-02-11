# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left != right:
            mid = math.ceil((left+right) / 2)

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid

        if isBadVersion(left):
            return left
        else:
            return left + 1
