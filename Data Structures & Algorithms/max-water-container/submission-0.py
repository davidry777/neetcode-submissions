class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)

        # Brute Force Solution - O(n^2)
        # First loop starts first given bar
        # for i in range(n):
        #     # Second loop starts going thorugh each other bar besides bar i
        #     # This is to check which has min height and takes that to calc amount
        #     for j in range(i+1, n):
        #         minHeight = min(heights[i], heights[j])
        #         width = j - i
        #         area = minHeight * width
        #         maxArea = max(area, maxArea)

        # Intricate solution - Two pointers
        l, r = 0, n-1

        while l < r:
            minHeight = min(heights[l], heights[r])
            area = minHeight * (r - l)
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
