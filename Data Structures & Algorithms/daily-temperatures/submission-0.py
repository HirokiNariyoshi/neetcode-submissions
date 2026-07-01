class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # keep stack sorted
        # if stack order is violated, keep popping until it isn't

        result = [0] * len(temperatures)  # default 0 for days with no warmer future
        # THIS CREATES A LIST OF ZEROS by default
        
        stack = []  # stores indices, not temperatures

        for i, temp in enumerate(temperatures):
            # while current temp is warmer than what's on top of stack
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j  # index distance = days to wait

            stack.append(i)

        return result
        # anything left in stack stays 0 (no warmer day found)