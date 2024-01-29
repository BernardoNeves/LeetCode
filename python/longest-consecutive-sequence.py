class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = 0
        m = 0
        for i in range(1, len(nums)):
            m +=1
            if nums[i] != nums[i-1]+1:
                n = max(n, m)
                m = 0
        return n
