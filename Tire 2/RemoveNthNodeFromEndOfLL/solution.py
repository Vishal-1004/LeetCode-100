# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        '''let us first understand the logic which we will be using to sovle this question
        concider the following linkedlist:
        5 -> 2 -> 7 -> 1 -> 9 -> 8 -> 3
        here if n = 3, so  we are suppose to remove the node with value as 9
        to do  we will use two pointer that is left and right, even before we do so we will have our dummy node at the top whose next node will be the head of the given linkedlist 
        
        now left points towards Dummy node initially and 
        right points towards the nth node from left that is
        dummy -> 5 -> 2 -> 7 -> 1 -> 9 -> 8 -> 3
        l                       r (r is 3 i.e n steps ahead of the head node)
        
        now one by one we will move left and right pointer in forward direction till right pointer reaches the end (None state)
        now the pointer positions will look as follows
        dummy -> 5 -> 2 -> 7 -> 1 -> 9 -> 8 -> 3 -> None
                                l                    r
                                
        thus we stop here and remove 9 by writing 
        left.next = left.next.next
        that is next node of 1 is next to next of it i.e 8
        thus our final linkedlist becomes
        dummy -> 5 -> 2 -> 7 -> 1 -> 8 -> 3
        
        hence we return dummy.next as our answer'''
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next