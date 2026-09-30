class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        # sort array

        # fix one entry, use 2 pointers
        
        nums.sort() # asc order
        length = len(nums) - 1
        print(nums)

        for i, num in enumerate(nums):
            left = i + 1
            right = length
            # ignore if nums[i] > 0 for valid triplets
            if nums[i] <= 0 and (nums[i] != nums[i-1] if i > 0 else 1):
                while right > left and i < left and i < right:
                    triplet_sum = nums[i] + nums[left] + nums[right]
                    # check 3sum==0, if so add to output
                    if triplet_sum == 0:
                        left_val = nums[left]
                        right_val = nums[right]
                        while (nums[left] == left_val) and right > left:
                            left += 1
                        while (nums[right] == right_val) and right > left:
                            right -= 1
                        output.append([nums[i], left_val, right_val])
                    elif triplet_sum > 0:
                        right -= 1
                    else:
                        left += 1
                

        return output







