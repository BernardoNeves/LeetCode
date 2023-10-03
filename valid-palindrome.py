import unittest


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        text = []
        for c in s:
            if c.isalnum():
                text.append(c.lower())

        lt = len(text)
        hlt = lt // 2
        rlt = lt % 2
        B = text[:hlt]
        C = text[hlt + rlt :][::-1]

        if B == C:
            return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_palindrome(self):
        s = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.isPalindrome(s))

    def test_non_palindrome(self):
        s = "race a car"
        self.assertFalse(self.solution.isPalindrome(s))

    def test_empty(self):
        s = " "
        self.assertTrue(self.solution.isPalindrome(s))

    def test_non_alphanumeric(self):
        s = " # $: @ ($:$ * ), ;"
        self.assertTrue(self.solution.isPalindrome(s))


if __name__ == "__main__":
    unittest.main()
