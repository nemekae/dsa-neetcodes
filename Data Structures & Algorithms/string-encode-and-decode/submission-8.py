class Solution:
    def __init__(self):
        self.delimiter = "Amara"

    # Use something as a delimeter in the list
    def encode(self, strs: List[str]) -> str:
        # Initialize encoded str
        encoded_str = ""

        # Build out the str
        for string in strs: 
            encoded_str += string + self.delimiter
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # Initialize decoded list
        decoded_list = s.split(self.delimiter)

        return decoded_list[:len(decoded_list)-1]