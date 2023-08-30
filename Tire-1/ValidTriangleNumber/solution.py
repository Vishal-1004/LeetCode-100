class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        '''if the length of the nums array is less than 3 then return 0'''
        if len(nums) < 3:
            return 0

        '''sorting the nums array in increasing order so that we can procede with two pointer approach'''
        nums.sort()
        '''running a for loop in reverse direction '''
        for i in range(len(nums)-1,1,-1):
            '''here we have 3 indexes i represents the last number which is the largest number 
            middle represents the index i-1
            first represents the index 0'''
            middle = i - 1
            first = 0

            '''running a while loop till first is less than middle'''
            while first < middle:
                '''now if nums[first] + nums[middle] > nums[i] it means that the property of the triangle is satisfied and we increment the count value by (middle - first) because concider the following example 
                [1,2,2,3,3,4] here it i represents 4 and middle -> 3 and first -> 2 
                so here the triangle condition is satisfied and as you can see other the entire set [2,2,3,3,4] follows the condition so we add (middle - first) [i.e no matter how many times we increment first value keeping middle as fixed the property of the triangel will still be satisfied] in count and then we reduce middle value by 1 assuming that it was too high to cross nums[i] with a large gap'''
                if nums[first] + nums[middle] > nums[i]:
                    count += (middle - first)
                    middle -= 1

                    '''else we assume that first was pointing towars an element which was small enought to not to corss nums[i] hence here we increment first by 1'''
                else:
                    first += 1

        return count