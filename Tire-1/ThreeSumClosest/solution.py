class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''maxValue stores infinty in it and ansValue is made to store the value closed to 
        the target'''
        maxValue = float('inf')
        ansValue = 0

        '''we are sorting the array to avoid concidering duplicate elements again and again 
        and after sorting only we can work with two pointers'''
        nums.sort()

        for i in range(len(nums)):
            ''''any ith index value which is similar to that of the previous one should be
            avoided because we have already solved for the scenario which come up with that valued element'''
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #left and right pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                value = nums[i] + nums[left] + nums[right]
                '''we are checking for the absolute difference between the value and the target value
                . If the difference is less than that of maxValue then we update maxValue and ansValue 
                eg: if target is 4 and value 3, then maxValue will become 1 and ansValue will be 3.
                Here 3 represents the value which is closer to target and maxValue gives the difference
                between the target and current value that is by how much value we are close to target.'''
                if abs(target - value) < maxValue:
                    maxValue = abs(target - value)
                    ansValue = value

                #if value turned out to be more than target then we have to move right pointer towards left by one
                elif value > target:
                    right -= 1
                
                #else left pointer has to be moved towards right because value was less than target
                else:
                    left += 1

        return ansValue
