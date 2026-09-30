class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # if all of the numbers leading up to the next number
        # sum to a negative, we want to omit them
        # so reset running sum to 0.
        running_sum = 0
        max_running_sum = float('-inf')

        for i, num in enumerate(nums):

            if running_sum < 0:
                running_sum = 0
            
            running_sum += num
            max_running_sum = max(running_sum, max_running_sum)
        return max_running_sum

