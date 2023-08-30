class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''initial content of the ansArr'''
        ansArr = [-1,-1]
        start = 0
        end = len(nums)-1

        '''at first we will try to find the left most occurance of the target elemlent in nums array
        inorder to do so when ever we get the target element at mid index then we shift our end pointer 
        at mid - 1 so that we can continue moving in left direction rahter than bothering about rigth side'''
        #left most occurence
        while start <= end:
            mid = (start+end)/2

            if nums[mid] == target:
                ansArr[0] = mid
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        '''now we will look for the right most occurance of the target element so again when we get 
        the element at the mid index then we make our start pointer to point towards mid + 1 so that 
        we can continue moving in forward direction'''
        #right most occurence
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)/2

            if nums[mid] == target:
                ansArr[1] = mid
                start = mid + 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1
        
        '''finally we return our answer '''
        return ansArr
            