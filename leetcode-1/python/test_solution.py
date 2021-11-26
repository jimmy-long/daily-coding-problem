from solution import Solution
import unittest

class ExampleTests(unittest.TestCase):

    def test_example_1(self):
        self.assertCountEqual([0, 1], Solution.two_sum([2, 7, 11, 15], 9))

    def test_example_2(self):
        self.assertCountEqual([1, 2], Solution.two_sum([3, 2, 4], 6))

    def test_example_3(self):
        self.assertCountEqual([0, 1], Solution.two_sum([3, 3], 6))

class CustomTests(unittest.TestCase):

    def test_no_answer(self):
        self.assertEqual(0, len(Solution.two_sum([1, 2, 3], 7)))

    def test_multiple_answers(self):
        self.assertCountEqual([0, 2], Solution.two_sum([1, 2, 4, 3], 5))

    def test_full_iteration(self):
        self.assertCountEqual([0, 5], Solution.two_sum([1, 2, 3, 4, 5, 9], 10))

if __name__ == '__main__':
    unittest.main()