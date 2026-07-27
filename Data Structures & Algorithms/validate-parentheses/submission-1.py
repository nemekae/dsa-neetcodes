class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { ")":"(","}":"{","]":"["}


        for char in s:
            if char not in brackets:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
            else:
                # If it's a closing bracket, check if it matches the last opening bracket
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop() 
                
        return len(stack) == 0


        



        