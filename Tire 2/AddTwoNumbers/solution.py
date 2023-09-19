# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        carry = 0

        '''while either l1 or l2 or carry is alive we will be continuing with our loop'''
        while l1 or l2 or carry:
            '''take the value of the respective node if the node is alive else take it as 0, 
            their might be a situation where l1.val and l2.val will both be equal to zero but will still would have some carry value to go with and if we dont have any value for carry then the while loop itself breaks'''
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry

            '''to understand the three lines gives below concider the following example 
            val = 125
            then carry = 125 // 10 = 12
            val = val % 10 = 5
            so next node gets values as 5 and now the carry becomes 12 and so on...'''
            #15 --> 1  5
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            '''updating the pointers'''
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next