Select tags
0/5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
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

        a = b = ListNode(None)
        for i in range(c-1,-1,-1):
            b.val = output[i].val
            if i == 0:
                pass
            else:
                b.next = ListNode()
            b = b.next
        return a
