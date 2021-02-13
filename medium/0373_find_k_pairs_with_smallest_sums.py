class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if (not nums1) or (not nums2):
            return []

        ret = []

        seen = set()
        next_pairs = {(0, 0, nums1[0]+nums2[0])}

        num_iterations = min(k, len(nums1)*len(nums2))

        for _ in range(num_iterations):
            # find the minimum pair that gives the smallest sum
            min_sum = float("inf")
            min_pair = (None, None)

            for i, j, sum_val in next_pairs:
                if sum_val < min_sum:
                    min_sum = sum_val
                    min_pair = (i, j)

            # append the minimum pair to the ret array
            i, j = min_pair
            ret.append([nums1[i], nums2[j]])

            # update next_pairs
            next_pairs.remove((i, j, min_sum))
            seen.add(min_pair)

            if (i+1 < len(nums1)) and ((i+1, j) not in seen):
                next_sum = nums1[i+1] + nums2[j]
                next_pairs.add((i+1, j, next_sum))

            if (j+1 < len(nums2)) and ((i, j+1) not in seen):
                next_sum = nums1[i] + nums2[j+1]
                next_pairs.add((i, j+1, next_sum))

        return ret
