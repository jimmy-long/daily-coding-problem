from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    @classmethod
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_head = ListNode()
        answer_pointer = answer_head

        pointer1 = l1
        pointer2 = l2

        carry = 0

        while pointer1 is not None or pointer2 is not None:
            val1 = pointer1.val if pointer1 is not None else 0
            val2 = pointer2.val if pointer2 is not None else 0

            sum = carry + val1 + val2

            answer_pointer.next = ListNode(sum % 10)

            pointer1 = pointer1.next if pointer1 is not None else None
            pointer2 = pointer2.next if pointer2 is not None else None
            answer_pointer = answer_pointer.next

            if (sum > 9):
                carry = sum // 10
            else:
                carry = 0
        
        if (carry > 0):
            answer_pointer.next = ListNode(carry)

        return answer_head.next