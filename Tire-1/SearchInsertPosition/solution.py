class Solution(object):

    def searchInsert(self, nums, target):
        '''we have created two indexes start and end which points at the starting and the ending
        position of the array and ansIndex is used to store the insertion index for and element
        which is not found in the array'''
        start,end = 0,len(nums)-1
        '''default value of the ansIndex is len(nums) becasue we assume that the element has to be
        inserted in the end of the array'''
        ansIndex = len(nums)

        '''runnig a while loop till start is less than or equal to end, here we have used equal to symbole
        also because array can be of size 1 also'''
        while start<=end:
            mid = (start+end)/2

            '''if element is present at the mid index then we return the mid value as the answer'''
            if nums[mid] == target:
                return mid

                '''if nums[mid] < target then we have to make start index as mid + 1 
                that is we will be moving in right direction '''
            elif nums[mid] < target:
                start = mid + 1

                '''now if nums[mid] > target then set ansIndex as mid and end as mid - 1
                , current element which is at mid index is greater than target so we can assume that 
                target must be inserted at index "mid" but to confirm this we change the end index as mid - 1
                so that again the while loop will run and will search that is their still any other element 
                between start and end which is greater than target or not'''
            else:
                ansIndex = mid
                end = mid - 1

        '''finally returning the answer index'''
        return ansIndex