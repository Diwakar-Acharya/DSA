# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if(not head or not head.next):
            return None;
        dummy = ListNode(0,head)
        temp = dummy

        slow = fast = head
        while fast and fast.next:
            temp = temp.next
            slow = slow.next
            fast = fast.next.next

        temp.next = slow.next

        return head

        
        