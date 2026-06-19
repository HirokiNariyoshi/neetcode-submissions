class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # use .append() & .pop()
        # add first char

        stack.append(s[0])

        for i, char in enumerate(s):
            print(stack)
            if i != 0:

                if stack:
                    is_closing = (stack[-1] == '[' and char == ']') or (stack[-1] == '(' and char == ')') or (stack[-1] == '{' and char == '}')
                else:
                    is_closing = False

                if is_closing:
                    stack.pop()
                elif char == '(' or char == '[' or char == '{':
                    stack.append(char)
                else:
                    return False




        if not stack:
            return True
        else:
            return False