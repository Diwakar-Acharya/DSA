class Solution:
    def insertionSortList(self, head: ListNode | None) -> ListNode | None:
        temp=head
        result=[]
        while temp:
            result.append(temp.val)
            temp=temp.next
        result.sort()
        dum=ListNode(0)
        curr=dum
        for i in result:
            curr.next=ListNode(i)
            curr=curr.next
        return dum.next
# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

#         dummy = ListNode(0)
#         curr = head

#         while curr:
#             nex = curr.next

#             prev = dummy

#             while prev.next and prev.next.val <= curr.val:
#                 prev = prev.next

#             curr.next = prev.next
#             prev.next = curr

#             curr = nex

#         return dummy.next
