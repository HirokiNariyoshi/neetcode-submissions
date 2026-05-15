class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, create a dict containing each letter and
        # its frequency. then, store this dict in another dict, with the
        # dict as the key and the value as the list containing the string.

        # if for a string, the dict (key) is found in the dict[dict[str]],
        # update the value of the dict[dict[str]] entry by appending the string to the list.

        dict_dict = {}

        for string in strs:

            freq_dict = {}   
            for char in string:
                if char in freq_dict:
                    freq_dict[char] += 1
                else:
                    freq_dict[char] = 1
            
            freq_dict = tuple(sorted(freq_dict.items()))

            if freq_dict in dict_dict:
                dict_dict[freq_dict].append(string)
            else:
                dict_dict[freq_dict] = []
                dict_dict[freq_dict].append(string)

        return list(dict_dict.values())





