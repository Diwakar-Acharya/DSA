# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: ListNode | None) -> ListNode | None:
        temp = head
        count = 0
        result = []

        
        
        while temp:
            if temp == None:
                return
            elif temp.val == 0:
                temp = temp.next
                while temp.val != 0:

                    count += temp.val
                    temp = temp.next
            else:
                while temp.val != 0:
                    count += temp.val
                    temp = temp.next

            temp = temp.next

            result.append(count)
            count = 0

        temp = head
        for num in result:
            temp.val = num
            prev = temp
            temp = temp.next
        prev.next = None

        return head
                