
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''this is a basic maths question which requires us to find the median of the sorted array becasue the median will be the closest number to reach by either incrementing or decrementing the remaining elements'''
        sortedArr = sorted(nums)
        median = sortedArr[int(len(nums)/2)]

        steps = 0
        '''for every element we are finding the absolute difference between the element and the mediam, then we are adding it into the steps count'''
        for i in sortedArr:
            steps += abs(i-median)

        return steps