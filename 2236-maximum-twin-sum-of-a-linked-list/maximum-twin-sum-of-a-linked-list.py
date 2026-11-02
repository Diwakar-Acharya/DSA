class Solution:
    def pairSum(self, head: ListNode | None) -> int:

        # Step 1: Find middle
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev = None
        curr = slow

        while curr:
            nexx = curr.next
            curr.next = prev
            prev = curr
            curr = nexx

        # Step 3: Calculate maximum twin sum
        result = 0
        temp = head

        while prev:
            result = max(result, temp.val + prev.val)

            temp = temp.next
            prev = prev.next

        return result