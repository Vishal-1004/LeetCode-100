# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        '''concider the following example 
        3 -> 2 -> 0 -> 4 -
             |           |
              -----------
        here after 4 we have 2 cycled with it so to discover this we will use two pointers namely 
        slow and fast 
        each of them will be intially pointing towards the head of the linkelist
        
        now the slow pointer will be jumping ahead one by one and 
        fast pointerw will be jumping two steps ahead 
        so if their is some cycle in the linkedlist then after certain number of jumps the slow and fast pointer will meet at a same point where as if their is now cycle then fast pointer will reach to NONE that is the last position of the last node'''
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False