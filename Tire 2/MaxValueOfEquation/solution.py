import heapq
class Solution(object):
    def findMaxValueOfEquation(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        '''useArr = []
        heapq.heapify(useArr)
        ans = float('-inf')

        for j in range(len(points)):
            while useArr and (points[j][0] - useArr[0][1] > k):
                heapq.heappop(useArr)

            if useArr:
                ans = max(ans,points[j][0] + points[j][1] - useArr[0][0])

            heapq.heappush(useArr,[-(points[j][1]-points[j][0]),points[j][0]])

        return ans'''
        '''here we are suppose to maximize (Yj + Yi + |Xj - Xi|), this can be rewritten as
        (Xj + Yj + (Yi - Xi)) and for this to be maximum:  (Yi - Xi) must be maximized.
        
        so for this reason we will be using monotonically decreasing queue to keep the track of max value of (Yi - Xi) and we will also store Xi along with it as we have to check whether the pair exceeds k or not.


        '''
        decreaseQ = deque()
        '''intial value of ans variable is -infinity'''
        ans = -sys.maxsize

        '''running a for loop in points to get Xj and Yj.'''
        for xj,yj in points:
            '''
            Note: decreaseQ = [[Yi - Xi, Xi]] is the format for it

            while the decreaseQ is not empty and Xj - Xi > k, here decreaseQ[0][1] = Xi
            so pop the left most element as its the heighest element becasue of which we are exceding k so we try to move towards lower value by poping our the left most value (the largest value of monotonically decreasing queue)
            '''
            while decreaseQ and xj - decreaseQ[0][1] > k:
                decreaseQ.popleft()

            '''after the above while loop if the decreaseQ is left with any element then it means that it follows Xj - Xi <= k rule, so now its time to check for the ans value that is 
            ans = max(ans, largest(Yi - Xi) + Xj + Yj)
            here largest value of (Yi - Xi) is nothing but the first element of the decreasing queue.'''
            if decreaseQ:
                ans = max(ans,decreaseQ[0][0] + xj + yj)

            '''now when ever a new element is added in the queue, the given below code is written to maintain the monotonical queue's property.
            here if new element that is Yj - Xj is greater than the last element of the decreaseQ then we must pop the last element of the queue and 
            this process has to be repeated till we get the correct position to insert it'''
            while decreaseQ and decreaseQ[-1][0] <= yj - xj:
                decreaseQ.pop()
            
            '''once the while loop we over we insert the values at its correct positon that is the last index'''
            decreaseQ.append((yj-xj,xj))

        '''finally returning the final answer'''
        return ans