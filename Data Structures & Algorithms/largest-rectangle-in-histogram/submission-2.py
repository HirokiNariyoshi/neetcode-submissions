class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # keep a monotonic stack where top is smallest element
        stack = []
        # store both height & position in stack
        max_area = 0

        for i, height in enumerate(heights):
            entry = [i, height]
            popped_delta = 0
            while stack and height < stack[-1][1]:
                popped_idx, popped_height = stack.pop()

                left_boundary = stack[-1][0] if stack else -1
                area = popped_height * (i - left_boundary - 1)
                max_area = max(max_area, area)

            stack.append(entry)
        
        # then calculate those that never got popped
        size = len(heights) - 1
        while stack:
            popped_idx, popped_height = stack.pop()
            if stack:
                left_boundary = stack[-1][0]
            else:
                left_boundary = -1
            area = popped_height * (size - left_boundary)
            max_area = max(max_area, area)         

        return max_area