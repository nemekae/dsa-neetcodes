class Solution:
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        total_sum = nums[0]

        for i in range(1, len(nums)):
            total_sum += nums[i]

            # Normal maximum subarray
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)

            # Minimum subarray
            curr_min = min(nums[i], curr_min + nums[i])
            min_sum = min(min_sum, curr_min)

        # Important edge case: all numbers are negative
        if max_sum < 0:
            return max_sum

        return max(max_sum, total_sum - min_sum)

