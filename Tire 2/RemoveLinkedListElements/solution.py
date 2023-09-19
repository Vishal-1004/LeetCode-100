# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        '''their might be some situation where they would have given us some empty linkelist head for that reasons we have kepth this below condition'''
        if head is None:
            return 

        '''prev pointer is used to keep the track of previous node and current_node is one step ahead of prev node'''
        prev = head
        current_node = prev.next

        '''while current_node is alive and if current_node.val == val then we must remove that current_node and for that reason we are doing prev.next = current_node.next
        in this way we can get rid of current_node,
        now we must move one step ahead so we do current_node = current_node.next, thus moving forward
        here we didn't had any need to move forward the prev node cause the middle node that is prev,(current_node),current_node.next was removed 
        
        but if the current_node.val is not equal to given val then prev node has to be moved forward along with current_node'''
        while current_node:
            if current_node.val == val:
                prev.next = current_node.next
            else:
                prev = prev.next
            current_node = current_node.next

        '''since in the start we didn't checked for the head value so we are doing it now '''
        if head and head.val == val:
            print("In if condition")
            return head.next
        return head