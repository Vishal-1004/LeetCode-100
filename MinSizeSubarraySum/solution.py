class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        '''here we are going to use two pointer approach to make a sliding window, this is why we have used i and j pointer. Here j  will keep on moving in rigth side until  it reached the end the of the array and we have even kept a "mn" variable which keeps a reacord of minimum length of sub array initially it is set to max integer possible. "sum" variable is used to find the sum of the subarray which we will be creating during our loop.'''
        i=0
        j=0
        sum=0
        mn=float("inf")

        while j<len(nums):
            sum += nums[j]
            '''here as you can see nums[j] is added every time in sum and it this sum in greater than or equal to the target value then we start to move our i pointer towards the right till the sum become less than the target and mean while we even keep a track of the min length of the subarray as shown below.'''
            while sum >= target:
                sum -= nums[i]
                mn = min(j-i+1,mn)
                i += 1

            j += 1
            '''if the sum is not equal to or greater than target then we just keep on incrementing j by 1'''
        
        '''if the mn value remains infinity it means that their is no such subarray possible hence return 0 else return the min length of the subarray.'''
        if mn == float("inf"):
            return 0
        else:
            return mn