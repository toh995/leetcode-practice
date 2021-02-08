class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        previous_max = previous_val = -1

        for i in range(len(arr)-1, -1, -1):
            new_val = max(previous_max, previous_val)

            previous_val = arr[i]
            previous_max = new_val

            arr[i] = new_val

        return arr
