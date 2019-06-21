import add_two_numbers
import pytest


def test_add_two_numbers():
    n1 = add_two_numbers.ListNode(2)
    n2 = add_two_numbers.ListNode(4)
    n3 = add_two_numbers.ListNode(3)
    n1.next = n2
    n2.next = n3

    n4 = add_two_numbers.ListNode(5)
    n5 = add_two_numbers.ListNode(6)
    n6 = add_two_numbers.ListNode(4)
    n4.next = n5
    n5.next = n6

    n7 = add_two_numbers.ListNode(7)
    n8 = add_two_numbers.ListNode(0)
    n9 = add_two_numbers.ListNode(8)
    n7.next = n8
    n8.next = n9

    assert add_two_numbers.Solution().add_two_numbers(n1, n4).val == n7.val
    assert add_two_numbers.Solution().add_two_numbers(n1, n4).next.val == n7.next.val
    assert add_two_numbers.Solution().add_two_numbers(n1, n4).next.next.val == n7.next.next.val
