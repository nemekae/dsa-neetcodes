class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> list[str]:
        """Decodes a single string back to a list of strings."""
        result = []
        i = 0
        n = len(s)

        while i < n:
            # Find the delimiter '#'
            j = s.index("#", i)
            
            # Find the lenght and turn to string
            length = int(s[i:j])

            # skip "#"
            j += 1
            
            result.append(s[j:j + length])
            i = j + length

        return result