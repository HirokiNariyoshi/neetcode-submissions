class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        # build prefix array    
        current_product = 1
        for num in nums:
            prefix.append(current_product)
            current_product = current_product * num
        
        current_product = 1
        size = len(nums)
        for i in range(size):
            suffix.append(current_product)
            current_product = nums[size - 1 - i] * current_product

        result = []
        suffix.reverse()
        for i in range(size):
            result.append(suffix[i] * prefix[i])
        
        return result

    
