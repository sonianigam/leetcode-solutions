class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)

        num_sum = str(num1 + num2)
        next_node = None
        head = None

        for d in num_sum:
            head = ListNode(int(d))
            head.next = next_node
            next_node = head

        return head

    def get_number(self, head = ListNode):
        node = head
        digits = []

        while node != None:
            digits.append(str(node.val))
            node = node.next

        num = "".join(digits)
        r_num = int(num[::-1])

        return r_num
