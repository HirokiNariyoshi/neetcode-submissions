class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            # 1. Move the left pointer rightward if it points to a non-alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
                
            # 2. Move the right pointer leftward if it points to a non-alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 3. Compare the characters
            if s[left] != s[right]:
                return False
            
            # 4. Move both pointers inward to check the next pair
            left += 1
            right -= 1

        return True
            