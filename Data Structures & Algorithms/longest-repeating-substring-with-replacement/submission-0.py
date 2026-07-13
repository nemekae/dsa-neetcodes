class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        max_len = 0
        n = len(s)

        for target in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            left = 0
            changes = 0

            for right in range(n):
                if s[right] != target:
                    changes += 1
                
                while changes > k and left <= right:
                    if s[left] != target:
                        changes -= 1
                    left += 1
                
                max_len = max(max_len, right - left + 1)
            
        return max_len

        