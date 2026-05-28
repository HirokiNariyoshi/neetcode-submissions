class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        answer = []

        while left < right:
            twosum = numbers[left] + numbers[right]

            if twosum == target:
                return [left + 1, right + 1]
            elif twosum < target:
                left += 1
            elif twosum > target:
                right -= 1
