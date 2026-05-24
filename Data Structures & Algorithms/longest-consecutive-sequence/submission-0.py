class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:           # iterate set to avoid duplicate work
            if num - 1 not in nums_set:   # sequence start
                length = 1
                while num + length in nums_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len



