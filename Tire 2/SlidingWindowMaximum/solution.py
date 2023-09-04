import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        '''here if we just use normal sliding window and find max element form each window then the overall time complexity becomes O(n**2) because total number of windows which will be formed will be = (n-k+1) and time taken to find max from each window will become O((n-k+1)*k) which is not accepted so we will go for the following approach 
        
        concider the following example 
        [8,7,6,9] and k=2
        her our first sliding window will be [8,7] since here max element is 8 so we add it in the output array
        now we remove 8 and add 6 in the array, again element at 0 index is greater so  we return  it 
        now we remove 7 and add 9 in the array since 9 is greter than 6 so we must remove 6 as we are making a queue whose left most element always has the largest element 
        this is how monotonically decreasing queue works
        
        when ever we add new element to it we must remove all the element which are smaller than the new element till we reach the last element or we get an element which is greater than the new element'''
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            '''if the queue is not empty and top most element of the queue is  less than the new element which we are going to add, then we pop the top most element form the queue, this process goes in a while loop'''
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            '''finally we add the new element which is at the index r'''
            q.append(r)
            
            '''if the left index is more than the index present at 0th index in queue then we pop out the left most element from the queue, this is done to show that we are moving in the right direction, this condition wont be executed only for the first time when we are making our first sliding window else it will keep on executing again and again everytime'''
            if l > q[0]:
                q.popleft()

            '''if our k is 2 so initially this condition wont run for one times because r value will be 0 first then 1 
            after than the value of r becomes 2,3,4,... and this conditon will run every time. The reason for this is that after first iteration we will keep on getting a sliding window and we have to put the max value that is always the left most value from the queue in the output array'''
            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output