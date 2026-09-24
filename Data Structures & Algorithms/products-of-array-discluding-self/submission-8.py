class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        max_product = 0
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                if max_product == 0:
                    max_product = num 
                else:
                    max_product = num * max_product
        
        if zero_count > 1:
            # every term will be 0
            return [0] * len(nums)
        
        result = []

        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(max_product // num)
            else:
                result.append(max_product)

        return result

    
