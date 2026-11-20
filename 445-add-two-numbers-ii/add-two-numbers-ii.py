class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None

        while s1 or s2 or carry:

            total = carry

            if s1:
                total += s1.pop()

            if s2:
                total += s2.pop()

            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head