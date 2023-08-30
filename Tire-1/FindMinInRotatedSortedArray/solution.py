class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''here in the question its clearly written that we are suppose to solve this question in O(log n) time complexity, which means that we are suppose to solve this qusetion using binary search operation'''
        '''at first we have created two pointers left and right which points towards the very ends of the array'''
        left = 0
        right = len(nums)-1

        '''this while loop has to be processed till left is less than right '''
        while left<right:
            '''then we are calculating mid value using the given below formula we can also use the formula "mid = (left+right)/2" to find the mid value.'''
            mid = left + (right - left)/2

            '''if the value at the mid index is more than the value at right index then we can say that we will be finding out our minimum value in the right side of the array so updating the left pointer as mid + 1, and continuing with the while loop'''
            if nums[mid] > nums[right]:
                left = mid + 1
                '''else we can say that the minimum value lies at the left side of the array so we make the right pointer as mid ans continue with our while loop'''
            else:
                right = mid

        '''at the end of the while loop we will get our minimum element at left index,
        you can verify this with the help of an example'''
        return nums[left]
