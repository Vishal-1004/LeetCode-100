# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return

        '''getting the lenght of the LL as well as the tail node'''
        length,tail = 1,head
        while tail.next:
            tail = tail.next
            length += 1
        
        '''by doing the below operation we get the k value within the length range that is if k is > lenght then by doing k % length we get a new k value which is < length'''
        k = k % length
        '''if k value gets converted into zero then it means that we will get the same LL even after we rotate it so, we normally return the head '''
        if k == 0:
            return head
        
        '''finding the kth node after which we have to rotate that is
        if LL given to us is
        3 -> 8 -> 1 -> 9 -> 4 -> 5
        and k is 2 then k = k % length is still 2 
        and node with value 9 is the node from where we are suppose to break and move the remaining node in front of the LL'''
        curr= head
        for i in range(length-k-1):
            curr = curr.next
        
        '''concidering the above example curr value right now is 9
        so newHead = curr.next = 4 -> 5
        and curr.next = None means 9 -> None
        and here tail is pointing towards the last node that is 5 so 
        tail.next = head which means 5 -> 3 -> ....
        
        hence our LL with newHead looks as follows:
        4 -> 5 -> 3 -> 8 -> 1 -> 9
        thus we return it'''
        newHead = curr.next
        curr.next = None

        tail.next = head

        return newHead