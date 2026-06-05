class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []

        # create window from [0].
        # expand window, but when a dupe is hit, shrink window from left
        # until the duped letter is removed

        max_length = 0

        for char in s:

            while char in window:
                window.pop(0)

            window.append(char)

            max_length = max(max_length, len(window))

        return max_length




















