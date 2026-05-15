class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_list = []
        for num in nums:
            if num in seen_list:
                return True
            seen_list.append(num)
        return False