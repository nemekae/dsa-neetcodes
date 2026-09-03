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
        output = ""
        i = 0
        n = len(s)

        while i < n:
            if s[i] != "#":
                output += s[i]
                i += 1
            else:
                output = int(output)
                word = s[i+1 : i+1+output]
                result.append(word)
                i = i + 1 + output
                output = ""

        return result