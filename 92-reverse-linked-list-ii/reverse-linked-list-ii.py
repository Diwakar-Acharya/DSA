# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before left
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        # Reverse the sublist using head insertion
        for _ in range(right - left):
            nex = curr.next

            curr.next = nex.next
            nex.next = prev.next
            prev.next = nex

        return dummy.next