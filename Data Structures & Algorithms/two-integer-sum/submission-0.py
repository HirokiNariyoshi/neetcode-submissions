class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_map = {}
        answer = []

        for i, num in enumerate(nums):
            j = target - num
            if j in seen_map:
                answer.append(seen_map[j])
                answer.append(i)
                return answer
            seen_map[num] = i

        return answer


        