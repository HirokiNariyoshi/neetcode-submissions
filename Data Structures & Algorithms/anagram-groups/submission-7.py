class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = {}
        # key: freq dict as tuple, sorted
        # value: word

        for word in strs:
            freq_dict = {}

            for char in word:
                if char in freq_dict:
                    freq_dict[char] += 1
                else:
                    freq_dict[char] = 1
            
            freq_dict = sorted(freq_dict.items())
            freq_key = tuple(freq_dict)

            if freq_key in freq_map:
                freq_map[freq_key].append(word)
            else:
                freq_map[freq_key] = [word]

        return list(freq_map.values())







