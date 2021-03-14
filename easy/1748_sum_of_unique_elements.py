class Solution:
    # no "cheating"
    def sumOfUnique(self, nums: List[int]) -> int:
        sum_val = 0
        seen_once = set()
        seen_twice = set()

        for num in nums:
            if num in seen_once:
                sum_val -= num
                seen_once.remove(num)
                seen_twice.add(num)

            elif num in seen_twice:
                continue

            else:
                sum_val += num
                seen_once.add(num)

        return sum_val


    # python easy solution
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(key for key in counter.keys() if counter[key] == 1)
