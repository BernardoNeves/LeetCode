import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertFalse(self.solution.containsDuplicate([]))

    def test_no_duplicates(self):
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4, 5]))

    def test_single_element(self):
        self.assertFalse(self.solution.containsDuplicate([1]))
        self.assertTrue(self.solution.containsDuplicate([1, 1]))

    def test_multiple_duplicates(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1, 4, 5, 2]))

    def test_large_input(self):
        input_list = [i for i in range(10**6)] 
        self.assertFalse(self.solution.containsDuplicate(input_list))

        input_list_with_duplicate = input_list + [0]
        self.assertTrue(self.solution.containsDuplicate(input_list_with_duplicate))


if __name__ == "__main__":
    unittest.main()
