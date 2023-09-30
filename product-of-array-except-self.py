import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]

        ans = 1
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= ans * nums[i + 1]
            ans *= nums[i + 1]
        return answer


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        nums = [7, 3, 5, 6]
        expected_result = [90, 210, 126, 105]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_result)

    def test_negative(self):
        nums = [-1, 1, 2, -3, 3]
        expected_result = [-18, 18, 9, -6, 6]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_result)

    def test_zero(self):
        nums = [-2, 1, 0, 4, 3]
        expected_result = [0, 0, -24, 0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_result)

    def test_only_zero(self):
        nums = [0, 0]
        expected_result = [0, 0]
        self.assertEqual(self.solution.productExceptSelf(nums), expected_result)


if __name__ == "__main__":
    unittest.main()
