class Solution:
    def splitListToParts(self, head: ListNode | None, k: int) -> list[ListNode | None]:

        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        x = count // k
        r = count % k

        result = []
        curr = head

        for i in range(k):
            part = curr
            size = x + (1 if i < r else 0)

            for j in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node

            result.append(part)

        return result