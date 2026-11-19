import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1


        # min-heap by default
        heap = []
        num_set = set()

        for entry in list(count.items()):
            flipped_entry = [entry[1], entry[0]]
            heapq.heappush(heap, flipped_entry)

        num_elements = len(heap)
        while num_elements > k:
            removed = heapq.heappop(heap)
            num_elements -= 1

        return [element[1] for element in heap]
