import unittest

from solution import ListNode
from solution import Solution

from typing import Optional

class ExampleTests(unittest.TestCase):

    def assert_linked_lists_equal(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        self.assertEqual( l1.val, l2.val )

        if l1.next is None and l2.next is None:
            return True

        if l1.next is not None:
            self.assertIsNotNone( l2.next )
        else:
            return False

        return self.assert_linked_lists_equal( l1.next, l2.next )

    def test_example_1(self):
        l1 = ListNode(val = 2)
        l1.next = ListNode(val = 4)
        l1.next.next = ListNode(val = 3)

        l2 = ListNode(val = 5)
        l2.next = ListNode(val = 6)
        l2.next.next = ListNode(val = 4)
        
        expected = ListNode(val = 7)
        expected.next = ListNode(val = 0)
        expected.next.next = ListNode(val = 8)

        self.assert_linked_lists_equal( expected, Solution.add_two_numbers( l1, l2 ) )

    def test_example_2(self):
        l1 = ListNode()
        l2 = ListNode()

        expected = ListNode(0)

        self.assert_linked_lists_equal( expected, Solution.add_two_numbers( l1, l2 ) )

    def test_example_3(self):
        l1 = ListNode(val = 9)
        l1.next = ListNode(val = 9)
        l1.next.next = ListNode(val = 9)
        l1.next.next.next = ListNode(val = 9)
        l1.next.next.next.next = ListNode(val = 9)
        l1.next.next.next.next.next = ListNode(val = 9)
        l1.next.next.next.next.next.next = ListNode(val = 9)

        l2 = ListNode(val = 9)
        l2.next = ListNode(val = 9)
        l2.next.next = ListNode(val = 9)
        l2.next.next.next = ListNode(val = 9)

        [8,9,9,9,0,0,0,1]
        expected = ListNode(val = 8)
        expected.next = ListNode(val = 9)
        expected.next.next = ListNode(val = 9)
        expected.next.next.next = ListNode(val = 9)
        expected.next.next.next.next = ListNode(val = 0)
        expected.next.next.next.next.next = ListNode(val = 0)
        expected.next.next.next.next.next.next = ListNode(val = 0)
        expected.next.next.next.next.next.next.next = ListNode(val = 1)

        self.assert_linked_lists_equal( expected, Solution.add_two_numbers( l1, l2 ) )

if __name__ == '__main__':
    unittest.main()