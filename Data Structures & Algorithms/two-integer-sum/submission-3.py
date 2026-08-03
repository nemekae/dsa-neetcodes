class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i,num in enumerate(nums):
            addon = target - num

            if addon in hashmap:
                return [hashmap[addon], i]
            
            hashmap[num] = i
        
        return None