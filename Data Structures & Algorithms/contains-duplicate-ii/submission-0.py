class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()

        for i,num in enumerate(nums):
            if num in windows:
                return True
            
            windows.add(num)

            if len(windows) > k:
                windows.remove(nums[i - k])
        
        return False
        