import add_two_numbers
import pytest


def test_add_two_numbers():
    n1 = add_two_numbers.ListNode(1)
    n2 = add_two_numbers.ListNode(2)
    n1.next = n2

    n3 = add_two_numbers.ListNode(3)
    n4 = add_two_numbers.ListNode(4)
    n3.next = n4

    n5 = add_two_numbers.ListNode(4)
    n6 = add_two_numbers.ListNode(6)
    n5.next = n6

    assert add_two_numbers.Solution().add_two_numbers(n1, n3).val == n5.val
    assert add_two_numbers.Solution().add_two_numbers(n1, n3).next.val == n5.next.val
