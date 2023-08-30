class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        '''suppose we have numbers like 7 and 5 then the range is 7,6 and 5. Their binary respresentation can be done as:
        111
        110
        101
        now if we take bitwise AND of all these numbers we will get 100 that is 4, from this you can note that this is nothing but the common bits available between 7 and 5 from the left hand side that is 
        111
        101 have only 100 in common 
        similary concider that range 12 to 15 we get
        1111
        1110
        1101
        1100 now bitwise AND of all these number will give us 1100 as the answer that is nothing but the common prefix between 15 and 12.
        So this question is finally resolved into finding of common prefix between the left and right limits given to us.
        '''
        moveFactor = 0
        while left != right:
            '''we will be right shifting both left and right elements by 1 every time till they become equal'''
            left >>= 1
            right >>= 1
            moveFactor += 1

        '''finally return left shift of left limit for moveFactor times as the answer'''
        return left << moveFactor