class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            # Use a length-prefix approach to handle cases where the delimiter is in the string
            encoded_string += str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            # Find the delimiter to get the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # Extract the string based on the parsed length
            decoded_strings.append(s[j+1 : j+1+length])
            i = j + 1 + length

        return decoded_strings
