# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        while curr and curr.next:
            check = curr.next
            if curr.val == check.val:
                curr.next = check.next
            else:
                curr = curr.next
        return head



