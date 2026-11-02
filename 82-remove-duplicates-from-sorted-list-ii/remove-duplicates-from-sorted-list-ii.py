# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import Counter

class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:

        temp = head
        s = []

        while temp:
            s.append(temp.val)
            temp = temp.next

        c = Counter(s)

        dummy = ListNode(0)
        curr = dummy

        temp = head

        while temp:
            if c[temp.val] == 1:
                curr.next = ListNode(temp.val)
                curr = curr.next

            temp = temp.next

        return dummy.next


        
        