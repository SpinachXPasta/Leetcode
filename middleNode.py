# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        a = b = ListNode(None)
        output = {}
        c = 0
        while True:
            if head == None:
                break
            else:
                b.val = head.val
                b.next = head.next
                output[c] = ListNode(head.val)
                head = head.next
                b = b.next
                c += 1

        if c < 2:
            return a
        
        if c % 2 != 0:
            K = int(ceil(c/2))
        else:
            K = int((c / 2) + 1)
        a = b = ListNode(None)
        for i in range(K-1,c):
            b.val = output[i].val
            if i == c-1:
                pass
            else:
                b.next = ListNode()
            b = b.next
        return a
