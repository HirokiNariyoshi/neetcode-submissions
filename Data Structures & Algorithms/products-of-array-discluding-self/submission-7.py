class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        total_product = 1
        nonzero_product = 1

        zero_encountered = False
        
        for num in nums:
            if num == 0 and zero_encountered:
                nonzero_product = 0
            elif (num != 0):
                nonzero_product *= num
            elif num == 0 and not zero_encountered:
                zero_encountered = True

            total_product *= num

        for num in nums:
            if num != 0:
                # Integer Division: //
                product = total_product // num
            else:
                product = nonzero_product
            result.append(product)

        return result