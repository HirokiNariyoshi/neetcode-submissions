class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # set of dicts, dict: key (number) value (index)
        seen_set = {}
        # set of just the values
        seen_val_set = set()

        for i, num in enumerate(numbers):

            if target - num in seen_val_set:
                return [seen_set[target - num] + 1, i + 1]

            seen_set[num] = i
            seen_val_set.add(num)


        