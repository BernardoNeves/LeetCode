class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previous_map = {}
        for index, current_num in enumerate(nums):
            prev = previous_map.get(target - current_num)
            if prev is not None:
                return [prev, index]
            previous_map[current_num] = index
