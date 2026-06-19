class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        list_size = len(nums)

        for i, num in enumerate(nums):
            right = i + k
            if right < list_size + 1:
                window = nums[i:right]
                max_of_window = max(window)
                result.append(max_of_window)

        return result