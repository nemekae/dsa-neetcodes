class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            # Current container's water = min height * width
            width = right - left
            current_height = min(heights[left], heights[right])
            max_water = max(max_water, current_height * width)

            # Move the pointer at the shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water


