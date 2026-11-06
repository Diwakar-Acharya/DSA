class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if not head or not head.next or k == 0:
            return head

        # Find length and tail
        count = 1
        tail = head

        while tail.next:
            tail = tail.next
            count += 1

        # Optimize rotations
        k = k % count

        if k == 0:
            return head

        # Make circular linked list
        tail.next = head

        # Find new tail
        steps = count - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Break circular connection
        new_head = new_tail.next
        new_tail.next = None

        return new_head