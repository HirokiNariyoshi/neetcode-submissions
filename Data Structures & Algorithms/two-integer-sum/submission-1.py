class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        ans = []

        for i, num in enumerate(nums):
            if target - num in seen_dict:
                return [seen_dict[target - num], i]

            seen_dict[num] = i

        