class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        nums=set(nums)
        prev=dummy
        current=head
        while current:
            if current.val in nums:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        return dummy.next