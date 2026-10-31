class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        result = 0
        curr = head

        while curr:
            result = result * 2 + curr.val
            curr = curr.next

        return result