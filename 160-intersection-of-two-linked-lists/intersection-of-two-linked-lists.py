class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        a = headA
        b = headB

        while a is not b:

            if a is None:
                a = headB
            else:
                a = a.next

            if b is None:
                b = headA
            else:
                b = b.next

        return a

# class Solution:
#     def getIntersectionNode(self, headA, headB):

#         seen = set()

#         while headA:
#             seen.add(headA)
#             headA = headA.next

#         while headB:
#             if headB in seen:
#                 return headB

#             headB = headB.next

#         return None