# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = 0
        num2 = 0
        temp1 = l1
        temp2 = l2


        while temp1:
            num1 = num1 * 10 + temp1.val
            temp1 = temp1.next
        while temp2:
            num2 = num2 * 10 + temp2.val
            temp2 = temp2.next
        num3 = num1 + num2

        
        dummy = ListNode(0)
        temp = dummy

        for digit in str(num3):
            temp.next = ListNode(int(digit))
            temp = temp.next

        return dummy.next