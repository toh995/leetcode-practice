class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == 1:
            return arr

        # binary search
        left = 0
        right = len(arr) - 1

        while (left + 1) != right:
            mid = (left + right) // 2

            if arr[mid] == x:
                left = mid
                right = left + 1
                break

            if x < arr[mid]:
                right = mid

            else:
                left = mid

        left_ret = []
        right_ret = []

        for _ in range(k):
            if left < 0:
                right_ret.append(arr[right])
                right += 1
                continue

            if right >= len(arr):
                left_ret.append(arr[left])
                left -= 1
                continue

            l_distance = abs(arr[left] - x)
            r_distance = abs(arr[right] - x)

            if l_distance <= r_distance:
                left_ret.append(arr[left])
                left -= 1
                continue

            else:
                right_ret.append(arr[right])
                right += 1
                continue

        left_ret.reverse()

        return left_ret + right_ret
