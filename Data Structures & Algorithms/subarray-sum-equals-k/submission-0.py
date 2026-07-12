from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1          # empty prefix, handles subarrays starting at index 0
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            # if (prefix_sum - k) has occurred before, those form valid subarrays ending here
            result += count[prefix_sum - k]
            count[prefix_sum] += 1

        return result