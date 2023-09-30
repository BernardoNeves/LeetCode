import unittest

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagrams(self):
        s = "listen"
        t = "silent"
        self.assertTrue(self.solution.isAnagram(s, t), msg="True")

    def test_not_anagrams(self):
        s = "hello"
        t = "world"
        self.assertFalse(self.solution.isAnagram(s, t), msg="False")

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""), msg="True, (both empty)")

    def test_different_lengths(self):
        s = "hello"
        t = "helloworld"
        self.assertFalse(self.solution.isAnagram(s, t), msg="False")

if __name__ == '__main__':
    unittest.main()
