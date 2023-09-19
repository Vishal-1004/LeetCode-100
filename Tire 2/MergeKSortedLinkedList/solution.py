# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    '''this is a basic method to merge two linkedlist and thus we return the merged linkedlist in sorted order from this method'''
    def mergeList(self,l1,l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            
            tail = tail.next
        
        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return 

        '''to reduce the time complexity as O(nlogK) where n is lenght of the linkedlist and k is the number of linkedlist given 
        we are following the given approach:
        here we are taking two linkedlist at a time and we are passing it to the merge function to get them merged and like wise we keep on doing so till the lists contains only one final linkedlist in it and that will be our answer.'''
        while len(lists) > 1:
            '''an empty and temp array to store the after results of the merged linkedlists which we will be getting'''
            mergedLists = []
            '''we will be running a for loop with a step of 2 cause we have to take two linkedlist at a time'''
            for i in range(0,len(lists),2):
                '''here l1 is lists[i] and if k is odd then we wont be having pairs of two-two linkedlist at a certain point so while assigning l2 we check that whether i + 1 is less than len(lists) or not if yes then l2 = lists[i+1] else None because having l2 as None wont make much of difference to us.'''
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                '''finally the merged linkedlist is appended in the temp array names mergedList'''
                mergedLists.append((self.mergeList(l1,l2)))
            
            '''we update the lists with all those new merged lists which we got '''
            lists = mergedLists
        
        '''finally the first index of the list is returned as that is our final merged linkedlist'''
        return lists[0]