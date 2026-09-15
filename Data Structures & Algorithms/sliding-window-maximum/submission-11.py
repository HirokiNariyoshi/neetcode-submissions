class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):

            # pop out indices from behind if they're smaller than the 
            # current element to the right
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                # ignore appending for elements when r has not spanned the full 
                # window size (in the beginning)
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output



            