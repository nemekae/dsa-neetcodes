class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { ")":"(","}":"{","]":"["}

        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0




        