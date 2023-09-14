from collections import deque
class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        here we intend to use monotonically increasing and descreasing queue 
        mono. increasing queue's top ( first element ) element is the min element of the given subarray and 
        mono. decreasing queue's top element is the max element of the given subarray
        these queue get updated every time we add an element in the subarray.

        In this way within O(n) time complexity we will be able to keep  track of max and min element of all the subarrays being formed at every time.

        Now the main idea is the 
        for every subarray being formed if we have the max and min element then we can just subtract them and check whether they are are than or equal to 2 or not,
        if yes then the whole subarray's element will follow our rule else we have to make necessary changes.

        Now if the condition is satisfied then r - l + 1 gives us the size of all subarrays
        which can be created while following the given condition.
        Here r and l is right and left index respectively of the sliding window.

        Now if the condition fails then 
        we will check that the element at the lth index is either max or min element if it is max or min element then we have to remove it from the respective queue else we will move the sliding window by incrementing l by 1.

        this process will be continued till r is less than len(nums).
        '''
        l = 0
        r = 0
        ans = 0
        maxQ = deque()
        minQ = deque()

        while r < len(nums):
            while maxQ and maxQ[-1] < nums[r]:
                maxQ.pop()

            while minQ and minQ[-1] > nums[r]:
                minQ.pop()

            maxQ.append(nums[r])
            minQ.append(nums[r])

            '''till the condition fails we check that the lth element is whether max's or min's queue's top  element or not, if yes we popleft from that queue else we move on to the next left element by increamenting it by one'''
            while maxQ[0] - minQ[0] > 2:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                if nums[l] == minQ[0]:
                    minQ.popleft()

                l += 1

            ans += (r-l+1)
            r += 1
        
        return ans
    
'''
monotonically increasing queue
(it means that the first element of the queue will be the smalles element and rest of the element will be in increasing order)

while minQ and minQ[-1] > nums[r]:
    minQ.pop()
minQ.append(nums[r])

here we run our while loop till maxQ is not empty and if last element is more than nums[r] then we have to pop out the last element as we are maintaining min elements queue
finally when the while loop gets over then we append nums[r] in the minQ


monotonically decreasing queue
(here the first element is the max element and rest of the element are in decreasing order)

while maxQ and maxQ[-1] < nums[r]:
    maxQ.pop()
maxQ.append(nums[r])
'''