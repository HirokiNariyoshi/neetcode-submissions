class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        # sorts by position, s as tiebreaker (s doesnt matter here)
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # it already belongs to a recorded fleet (top of stack)
                # so don't count it in the stack
                stack.pop()
        return len(stack)