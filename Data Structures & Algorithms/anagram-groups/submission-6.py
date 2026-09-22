class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = {}
        # key should be a freq tuple, value should be a list of indices
        
        for i, word in enumerate(strs):
            # in this loop i want to store letter frequency info,
            # as well as indices of those words in strs
            freq_dict = {}
            for char in word:
                if char not in freq_dict:
                    freq_dict[char] = 1
                else:
                    freq_dict[char] += 1
                
            freq_tuple = tuple(sorted(freq_dict.items()))

            if freq_tuple not in freq_map:
                freq_map[freq_tuple] = [i]
            else:
                freq_map[freq_tuple].append(i)

        
        output = []
        for index_list in freq_map.values():
            # in this loop i want to add them to the output
            entry = []

            for index in index_list:
                # print(index)
                entry.append(strs[index])

            output.append(entry)

        return output





