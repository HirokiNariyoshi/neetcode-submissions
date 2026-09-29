class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        
        max_heap = []
        arr_length = len(nums)

        for i, num in enumerate(nums):
            element = [(-1)*num, i]
            # push element onto max heap
            heapq.heappush(max_heap, element)

            if i >= k - 1 and i < arr_length:
                # make sure max in heap is within the window
                # print(max_heap)
                while(max_heap[0][1] < i - k + 1):
                    heapq.heappop(max_heap)
                output.append((-1) * max_heap[0][0])
        return output




            