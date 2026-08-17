from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            
        count = sum = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            sum += num
            count += seen[sum - k]
            seen[sum] += 1
        return count

    