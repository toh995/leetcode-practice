class Solution:
    # recursive
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []

        def helper(k):
            if k <= n:
                ret.append(k)
                k *= 10
                for i in range(10):
                    helper(k + i)

        for k in range(1, 10):
            helper(k)

        return ret


    # cusing string sort
    def lexicalOrder2(self, n: int) -> List[int]:
        '''
        Time: O(n + nlogn + n)
        Space: O(n)
        '''
        ret = [str(i) for i in range(1, n+1)]
        ret.sort()
        return [int(i) for i in ret]
