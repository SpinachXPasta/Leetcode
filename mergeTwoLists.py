# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #def ll(node):
        #    if node == None:
        #        return node
        #    else:
        #        return ListNode(node.val,ll(node.next))

        def ll(node1,node2):
            if node1 == None and node2 == None:
                return node1
            else:
                if node1 != None and node2 != None:
                    if node1.val < node2.val:
                        return ListNode(node1.val,ll(node1.next,node2))
                    else:
                        return ListNode(node2.val,ll(node1,node2.next))
                elif node1 != None and node2 == None:
                    return ListNode(node1.val,ll(node1.next,node2))
                elif node1 == None and node2 != None:
                    return ListNode(node2.val,ll(node1,node2.next))
                   
        
        #print (ll(list1,list2))
        return ll(list1,list2)
