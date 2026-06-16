class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = {}
        min_size = float("inf")

        # create a frequency list of chars in t

        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 1

        

        # Keep track of how many letters we've covered in the window
        need = len(t_freq)
        # these are counts of DISTINCT letters needed in the substring
        have = 0
                
        left = 0
        # move left if it's not a part of the freq list
        # OR if an entry in w_freq becomes negative

        w_freq = {} # frequency list of chars inside the window

        min_left = 0

        for i, char in enumerate(s):
            if char in w_freq:
                w_freq[char] += 1
            else:
                w_freq[char] = 1

            # did adding this char satisfy one more required char?
            if char in t_freq and w_freq[char] == t_freq[char]:
                # only increment have once the frequencies for this letter matches
                # the requirements
                have += 1

            # shrink from left while window is valid
            while have == need:
                # update minimum
                if (i - left + 1) < min_size:
                    min_size = i - left + 1
                    min_left = left

                # remove leftmost char
                left_char = s[left]
                w_freq[left_char] -= 1

                if left_char in t_freq and w_freq[left_char] < t_freq[left_char]:
                    have -= 1
                left += 1

        return s[min_left : min_left + min_size] if min_size != float("inf") else ""





