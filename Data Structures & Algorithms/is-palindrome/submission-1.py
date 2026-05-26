class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_array = list(s)

        for char in s:
            if not ((ord(char) <= 122 and ord(char) >= 97) or (ord(char) <= 57 and ord(char) >= 48)):
                s_array.remove(char)

        left = 0
        right = len(s_array) - 1

        while left < right:
            if s_array[left] != s_array[right]:
                return False
            left += 1
            right -= 1

        return True

            