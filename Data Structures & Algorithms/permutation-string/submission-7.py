class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1_dict = {}

        for char in s1:
            if char in s1_dict:
                s1_dict[char] += 1
            else:
                s1_dict[char] = 1
        
        window_size = len(s1)

        # create a sliding window as soon as a letter is hit 
        # in s2 that matches s1

        # shift left pointer when char is not found in s1

        window_dict = {}

        left = 0

        for i, char in enumerate(s2):
            
            window_dict[char] = window_dict.get(char, 0) + 1   

            if i >= window_size:
                left_char = s2[left]
                window_dict[left_char] -= 1

                if window_dict[left_char] == 0:
                    del window_dict[left_char]
                    
                left = i - len(s1) + 1


            if i >= window_size - 1:
                if window_dict == s1_dict:
                    return True
            
            
            left = i - len(s1) + 1


        return False