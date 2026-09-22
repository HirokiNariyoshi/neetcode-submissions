class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        # increase count iff a new letter not in dict is encountered 
        # otherwise left++, size = right - left + 1
        output = 0

        window_dict = {}

        for right, char in enumerate(s):
            if char not in window_dict:
                window_dict[char] = 1 
            else:
                window_dict[char] += 1

            # keep moving left pointer until no dupes remain
            while (window_dict[char] > 1):
                window_dict[s[left]] -= 1
                left += 1
            output = max(output, right - left + 1)

        return output