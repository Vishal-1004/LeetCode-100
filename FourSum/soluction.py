class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ansArr = []
        '''sorting the array to keep track of repeated elements'''
        nums.sort()
        '''our first for loop has to go till len(num)-3 because rest of the positions will be
        filled by remaining 3 numbers'''
        for i in range(len(nums)-3):
            '''if the number at ith position is same as that of i-1th position then we don't need 
            to consider this case becaue we have already solved using that element value so skip it'''
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            '''this for loop will go till len(nums)-2 becasue the other two numbers will be filled 
            by remaining two numbers'''
            for j in range(i+1,len(nums)-2):
                '''again we are skiping the repeated elements becasue we have already solved by
                considering those values'''
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                '''left and rigth pointers'''
                left = j+1
                right = len(nums) -1
                while left<right:
                    sumValue = nums[i]+nums[j]+nums[left]+nums[right]

                    '''if sumValue is more than that of target then decrease the right index value
                    because right points towards elemnets with higher value'''
                    if sumValue > target:
                        right -= 1

                        '''if sumValue is less than that of target then increase the left index value
                    because left points towards elemnets with lower value'''
                    elif sumValue < target:
                        left += 1
                    else:
                        ansArr.append([nums[i],nums[j],nums[left],nums[right]])
                        '''now in the given while loop we are trying to avoid repeated elements from both 
                        left and right directions'''
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return ansArr