class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        # key is the box number
        # value is the count of balls in that box
        boxes = {}

        for num in range(lowLimit, highLimit + 1):
            sum_val = 0

            while num > 0:
                digit = num % 10
                sum_val += digit
                num = num // 10

            if sum_val in boxes:
                boxes[sum_val] += 1
            else:
                boxes[sum_val] = 1

        return max(boxes.values())
