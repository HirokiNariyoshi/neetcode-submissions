class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_dict = {}

        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1

        # sort the list of frequencies in descending order
        frequency_list = list(frequency_dict.values())
        frequency_list.sort(reverse=True)

        answer = []

        for i in range(k):
            target_frequency = frequency_list[i]

            for key, value in frequency_dict.items():
                if value == target_frequency:
                    if key not in answer:
                        answer.append(key)
                        break

        return answer




    