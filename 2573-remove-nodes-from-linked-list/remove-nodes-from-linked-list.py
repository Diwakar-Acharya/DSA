class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:

        prev = None
        curr = head

        # Step 1: Reverse linked list
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        # Step 2: Remove nodes smaller than maximum
        temp = prev
        curr_max = float('-inf')

        dummy = ListNode(0)
        res = dummy

        while temp:
            if temp.val >= curr_max:
                curr_max = temp.val

                res.next = temp
                res = res.next

            temp = temp.next

        res.next = None

        # Step 3: Reverse result again
        curr = dummy.next
        prev = None

        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev