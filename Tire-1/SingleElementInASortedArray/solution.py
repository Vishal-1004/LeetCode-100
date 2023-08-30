class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''setting two pointer i and j as 0'''
        i = 0
        j = 0
        '''if the length of the array is one is them return that single element as the answer'''
        if len(nums) == 1:
            return nums[0]

        '''running a while loop till j reaches the end of the array'''
        while j < len(nums):
            '''if nums[i] == nums[j] then increment j by one as we are looking for the unique element'''
            if nums[i] == nums[j]:
                j += 1
            
                '''now if they both are not equal and if the difference between ith and jth index is 1 its means that the the sequecen would have been [2,2,3,4] here i would have been at 2nd index and j at 3rd index so here as you can see nums[i] and nums[j] is not equal and and j-i is 1 hence return nums[i]'''
            elif nums[i] != nums[j]:
                if j - i == 1:
                    return nums[i]
                else:
                    '''else make i to point towards j and continue'''
                    i = j

        '''if the while loop gets over then just return the last element as the answer'''
        return nums[j-1]
