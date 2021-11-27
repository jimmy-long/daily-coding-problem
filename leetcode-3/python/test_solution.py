import unittest

from solution import Solution

class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual( 3, Solution.length_of_longest_substring( "abcabcbb" ) )

    def test_example_2(self):
        self.assertEqual( 1, Solution.length_of_longest_substring( "bbbbb" ) )
    
    def test_example_3(self):
        self.assertEqual( 3, Solution.length_of_longest_substring( "pwwkew" ) )

    def test_example_4(self):
        self.assertEqual( 0, Solution.length_of_longest_substring( "" ) )

class CustomTests(unittest.TestCase):

    def test_all_unique(self):
        self.assertEqual( 7, Solution.length_of_longest_substring( "abcdefg" ) )

    def test_sandwich(self):
        self.assertEqual( 6, Solution.length_of_longest_substring( "abcdefa" ) )

    def test_one_char(self):
        self.assertEqual( 1, Solution.length_of_longest_substring( "a" ) )

if __name__ == "__main__":
    unittest.main()