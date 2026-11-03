class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:

        if not head or not head.next:
            return head

        # 1. Find middle
        slow = fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two halves
        prev.next = None

        # 3. Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # 4. Merge sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode(0)
        curr = dummy

        while left and right:

            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        curr.next = left if left else right

        return dummy.next