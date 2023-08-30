class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''we are sorting the array because our two pointers will be pointing towards
        the lower and the higher end, this sorting will also be helpful to find out
        duplicate elements and thus to avoid them'''
        nums.sort()
        ansArr = []

        #outer for loop to move in forward direction one by one
        for i in range(len(nums)):
            '''this if condition checks that we get any element repeated then we must 
            skip it because for the element with its value we have already performed 
            our operation of 3 sum'''
            if i>0 and nums[i-1] == nums[i]:
                #print("in if",i)
                continue
                #continue will make the for loop to go to the next element 
            
            j = i+1 # j is the left pointer pointing towards the element of lower value
            k = len(nums)-1 # k is the rigth pointer pointint towards the higher value
            while j<k:
                s = nums[i]+nums[j]+nums[k]

                if s>0:
                    '''if sum is greater than 0 then it means that the value of kth position
                    was too large so make the k to move in left direction so that we can get a 
                    lower value whose sum with the other two value (element at ith and jth
                    position) will be zero'''
                    k -= 1
                
                elif s<0:
                    '''if sum is less than 0 then it means that the value at jth position was
                    too small so move j in right direction to get a greater value.'''
                    j += 1

                else:
                    '''got the trriplet hence added it in the ansArr'''
                    ansArr.append([nums[i],nums[j],nums[k]])
                    '''now with the same ith element we are trying to find some other jth and kth
                    element which might even sum up to 0'''
                    j += 1
                    '''in the below while loop we are tyring to avoid duplicate numbers while moving
                    forward'''
                    while nums[j-1] == nums[j] and j<k:
                        j += 1
        return ansArr
