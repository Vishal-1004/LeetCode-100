class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''for finding out the last standing unique number from a given array, we can perform XOR operation on all the elements of the array. This is a property of XOR operation that if performed on all the elements of an array then we will be finally left with only an element which is nothing but the unique element form the array'''

        c = 0
        for i in nums:
            c = c ^ i

        return c