# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        #split the list into two halfs
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left,right)

    def getMid(self,head):
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self,left,right):
        tail = dummy = ListNode()

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        
        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next