class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        remove = set(nums)

        prev = dummy
        curr = head

        while curr:
            if curr.val in remove:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next