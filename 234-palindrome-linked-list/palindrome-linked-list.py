class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        # Step 1: Find the middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None
        curr = slow

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        # Step 3: Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True