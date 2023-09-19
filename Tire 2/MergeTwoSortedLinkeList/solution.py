# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        '''created a dummy node to start with'''
        dummy = ListNode()
        tail = dummy

        '''while both of the linkedlists are active'''
        while l1 and l2:
            '''if l1.val is less than l2.val then tail.next will point at l1 and now we will be looking at l1.next'''
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
                '''else taile.next will be l2 and we will move l2 pointer to l2.next'''
            else:
                tail.next = l2
                l2 = l2.next
            
            '''and here tail keeps on moving forward'''
            tail = tail.next

        '''if the while loop  got over due to the l2 linkedlist getting over then we will have to point tail.next to l1 else to l2'''
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        '''since dummy node's value is None so we must point to its next element as that was the node from where we started merging the two nodes'''
        return dummy.next
        