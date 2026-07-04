class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = left + ((right - left) // 2)

            value = nums[middle]
            if value > target:
                right = middle - 1
            elif value < target:
                left = middle + 1
            else:
                return middle

        return -1