class MinStack:

    def __init__(self):
        # two stacks, one for keeping track of min element
        self.min_stack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack: 
            val = min(val, self.min_stack[-1])

        # append val to min stack if it is smaller than the current min, otherwise
        # adds the current min again
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
