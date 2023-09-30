import unittest


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        top = []
        for num, count in counter:
            top.append(num)
            if len(top) == k:
                return top
        return top


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_topKFrequent_basic(self):
        nums = [4, 5, 4, 1, 1, 2, 2, 3, 1, 2, 3, 1]
        k = 2
        expected_result = [1, 2]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected_result)

    def test_topKFrequent_negative(self):
        nums = [0, -2, 3, 4, -1, 4, 2, -1, 2, 1]
        k = 2
        expected_result = [4, -1]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected_result)

    def test_topKFrequent_single_element(self):
        nums = [5]
        k = 1
        expected_result = [5]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected_result)

    def test_topKFrequent_large_k(self):
        nums = [1, 2, 3, 4, 5]
        k = 10
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected_result)


if __name__ == "__main__":
    unittest.main()
