class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''i is a pointer which points towards the index at which the next element has to be placed and count is the pointer which keeps the count of occurance of the element, initially it is one because we are concidering the element at index 0 has
        occured once'''
        i = 0
        count  = 1

        '''running a for loop from index 1 to len(nums)'''
        for j in range(1,len(nums)):
            
            '''if the element at jth index is same as that of element at index i and the count value has not yet exceded 2 then we perform i += 1 :- i.e we are incrementing the ith value and placing the element at jth index in it and also increasing the value of count'''
            if nums[i] == nums[j] and count < 2:
                count += 1
                i += 1
                nums[i] = nums[j]

                '''now if the element at jth index is not same as that of element at ith index then it means that the element has occured for the first time so the count value is made as 1 and then we perform the usual process'''
            elif nums[i] != nums[j]:
                count = 1
                i += 1
                nums[i] = nums[j]

                '''finally if the count value has reached 2 then we skip the element and move on to the next element'''
            else:
                continue
        
        return i + 1
