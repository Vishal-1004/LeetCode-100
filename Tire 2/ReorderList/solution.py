# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        '''the given below loop is used the find the point form where we have to break the array into two that is
        given LinkedList is
          1 -> 2 -> 3 -> 4
        slow  fast
        here slow move by one and fast moves by two so when fast reaches node 4
        slow would have reached node 2, so we can say that our second half start from the next node to node 2, i.e from node 3'''
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        '''here we are trying to reverse the second half '''
        second = slow.next
        slow.next = None
        prev = None

        # reverse second half
        while second:
            '''concider second half as 3 -> 4 -> 5
            and second = 3
            so temp = second.next = 4
            second.next = prev = none

            prev = second = 3
            second = temp = 3
            '''
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        '''finally we will merge the two LinkedList and we get our final answer'''
        #merge two half
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2