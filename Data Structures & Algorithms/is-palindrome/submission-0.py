class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        else:
            return True;