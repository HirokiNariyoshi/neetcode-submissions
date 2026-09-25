class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in num_set:
                # start of a new sequence
                seq_length = 1
                next_num = num + 1
                while next_num in num_set:
                    seq_length += 1
                    next_num += 1
                result = max(result, seq_length)
        return result




