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
        while i < len(s):
            # Find the delimiter '#' to read off the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # Extract exactly `length` characters as the next string
            start = j + 1
            result.append(s[start:start + length])

            i = start + length

        return result