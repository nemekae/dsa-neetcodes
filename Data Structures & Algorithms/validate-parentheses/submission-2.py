class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { ")":"(","}":"{","]":"["}


        for char in s:
            if char not in brackets:
                stack.append(char)
            else:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
        return len(stack) == 0

        



        