# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def reverseBetween(self, head, left, right):
#         dummy = ListNode(0)
#         dummy.next = head

#         prev = dummy

#         # Move prev to the node before left
#         for _ in range(left - 1):
#             prev = prev.next

#         curr = prev.next

#         for i in range(right - left):
#             nex = curr.next
#             for i in range(right - left - i):
#                 curr.val, nex.val = nex.val, curr.val
#                 nex = nex.next
            
#             curr = curr.next

#         return dummy.next


class Solution:
    def reverseBetween(self, head, left, right):

        curr = head
        prev = None

        # Reach left position
        for _ in range(left - 1):
            curr = curr.next

        left_node = curr

        # Reach right position
        for _ in range(right - left):
            curr = curr.next

        right_node = curr

        # Swap values moving inward
        while left_node != right_node:
            if left_node.next == right_node:
                break

            left_node.val, right_node.val = right_node.val, left_node.val

            left_node = left_node.next

            # Find previous node of right_node
            temp = head
            while temp.next != right_node:
                temp = temp.next

            right_node = temp

        if left_node == right_node:
            return head

        left_node.val, right_node.val = right_node.val, left_node.val

        return head