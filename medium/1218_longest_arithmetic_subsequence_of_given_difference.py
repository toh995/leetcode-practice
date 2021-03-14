class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # build map
        # key is a number in arr
        # val is an array of indexes for that number
        index_map = {}

        for index, num in enumerate(arr):
            if num in index_map:
                index_map[num].append(index)
            else:
                index_map[num] = [index]

        # calculates the length of the max subsequence starting at the given index
        @cache
        def helper(start_index: int) -> int:
            start_num = arr[start_index]
            next_num = start_num + difference

            # if we cannot build a further subsequence, just return 1
            if next_num not in index_map:
                return 1

            else:
                next_indexes = index_map[next_num]
                next_indexes = [index for index in next_indexes if index > start_index]

                # if we don't have any candidates for the next index, then return 1
                if not len(next_indexes):
                    return 1
                else:
                    return max(1+helper(index) for index in next_indexes)

        return max(helper(i) for i in range(len(arr)))
