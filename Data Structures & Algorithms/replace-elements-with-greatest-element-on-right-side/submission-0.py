class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1
        n = len(arr)

        for i in range(n - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)
        
        return arr