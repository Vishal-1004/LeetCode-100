class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        '''Here i acts as a pointer, the value of i increases only when we find some value 
        which is not same as that of "val". in the for loop we are trying to bring all the elements
        which are not equal to "val" in the left side and thus filturing all the remaining values'''
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != val:
                '''as you can see any element which is not equal to "val" is placed at the ith index
                and then i is incremented by one thus pointing to the next place where we will be keeping
                our next element which is not equla to  val'''
                nums[i] = nums[j]
                i += 1
        
        return i 