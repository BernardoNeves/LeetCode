class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = max(sum(piles) / h, 1)
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
