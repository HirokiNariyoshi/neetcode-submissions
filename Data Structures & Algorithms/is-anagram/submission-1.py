class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_1 = {}
        char_count_2 = {}

        for char1 in s:
            if char1 not in char_count_1:
                char_count_1[char1] = 1
            else:
                char_count_1[char1] += 1

        for char2 in t:
            if char2 not in char_count_2:
                char_count_2[char2] = 1
            else:
                char_count_2[char2] += 1    

        return char_count_1 == char_count_2