import unittest

class Solution(object):
    def groupAnagrams(self, strs):
        """

        :type strs: List[str]

        :rtype: List[List[str]]
        """
        strs_map = {}
        for word in strs:
            sorted_string = "".join(sorted(word))
            if sorted_string in strs_map:
                strs_map[sorted_string].extend([word])
            else:
                strs_map[sorted_string] = [word]
        return list(strs_map.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_input(self):
        self.assertEqual(self.solution.groupAnagrams([]), [])

    def test_single_anagram_group(self):
        input_strs = ["listen", "silent"]
        expected_output = [["listen", "silent"]]
        self.assertEqual(self.solution.groupAnagrams(input_strs), expected_output)

    def test_multiple_anagram_groups(self):
        input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(self.solution.groupAnagrams(input_strs), expected_output)

    def test_no_anagrams(self):
        input_strs = ["abc", "def", "xyz"]
        expected_output = [["abc"], ["def"], ["xyz"]]
        self.assertEqual(self.solution.groupAnagrams(input_strs), expected_output)

    def test_mixed_anagrams_and_non_anagrams(self):
        input_strs = ["abc", "bca", "def", "xyz", "cab"]
        expected_output = [["abc", "bca", "cab"], ["def"], ["xyz"]]
        self.assertEqual(self.solution.groupAnagrams(input_strs), expected_output)

if __name__ == '__main__':
    unittest.main()