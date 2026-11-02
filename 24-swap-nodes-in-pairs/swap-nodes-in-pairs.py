# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        # if head == None or head.next == None:
        #     return head
        # else:
        #     curr = head
        #     temp = head.next

        # while curr and temp:
        #     if temp.next == None or temp == None or curr == None:
        #         return head

        #     curr.val, temp.val = temp.val, curr.val
        #     curr = curr.next.next
        #     temp = temp.next.next


        # return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            curr = prev.next
            temp = curr.next

            curr.next = temp.next
            temp.next = curr
            prev.next = temp

            prev = curr

        return dummy.next
