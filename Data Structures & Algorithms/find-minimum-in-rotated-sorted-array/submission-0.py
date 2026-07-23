class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # this means that [left : middle] is sorted in asc.
                left = middle + 1
                # now we'll look at [middle : right]
            else:
                # this means that [middle : right] is sorted in asc.
                right = middle
                # now we'll look at [left : middle]

        return nums[left]

            
