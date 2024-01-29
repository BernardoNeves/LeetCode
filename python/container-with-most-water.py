class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            h_left = height[left]
            h_right = height[right]
            area = max(area, (right - left) * min(h_left, h_right))
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return area
