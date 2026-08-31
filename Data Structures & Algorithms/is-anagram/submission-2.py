class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_dict = {}

        for char in s:
            if char not in freq_dict:
                freq_dict[char] = 1

            else:
                freq_dict[char] += 1

        for char in t:
            if char not in freq_dict:
                return False

            else:
                freq_dict[char] -= 1
                
        if list(freq_dict.values()) == [0]*len(freq_dict):
            return True
        return False