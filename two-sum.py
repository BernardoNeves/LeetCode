import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previous_map = {}
        for index, current_num in enumerate(nums):
            diff = target - current_num
            if diff in previous_map:
                return [previous_map[diff], index]
            previous_map[current_num] = index
        return None

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum_found(self):
        nums = [8, 7, 11, 15, 2, 4]
        target = 9
        expected_result = [1, 4]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    def test_two_sum_not_found(self):
        nums = [3, 2, 5]
        target = 6
        expected_result = None
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        nums = []
        target = 9
        expected_result = None
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        expected_result = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()