
class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        if not head or not head.next:
            return

        # Step 1: Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        # Step 3: Merge two halves
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
