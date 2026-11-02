# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # store = []

        # temp = head
        # while temp and temp.next:
        #     store.append(temp)
        #     temp = temp.next.next

        # temp = head.next

        # while temp and temp.next:
        #     store.append(temp)
        #     temp = temp.next.next
        
        # temp = head

        # for i in range(len(store)):
        #     temp.val = store(i)
        #     temp = temp.next
        
        # return head
        if not head:
            return None

        store = []

        # Store odd-positioned nodes
        temp = head

        while temp:
            store.append(temp)
            temp = temp.next.next if temp.next else None

        # Store even-positioned nodes
        temp = head.next

        while temp:
            store.append(temp)
            temp = temp.next.next if temp.next else None

        # Reconnect nodes
        for i in range(len(store) - 1):
            store[i].next = store[i + 1]

        store[-1].next = None

        return store[0]

    



        