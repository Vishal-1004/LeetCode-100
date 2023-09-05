class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        '''lets understand this question with the help of any example
        here we will combine the position and speed of the cars together and write it 
        [[10,2],[8,4],[0,1],[5,1],[3,3]]
        and the target position is 12, now let us find the time taken to reach the target for each car and write it in an array
        [1,1,12,7,3] these are the times which are taken by the respective cars to reach the target
        
        now if we go in order, car1 and car2 reach target together in a fleet
        car3 will come alone as a single fleet 
        car4 and car5 come together as a fleet
        
        to understand this more clearly lest first sort the array in terms of their positions
        we get 
        [[0,1,12],[3,3,3],[5,1,7],[8,4,1],[10,2,1]]
        now look from right side 
        car at position 10 takes 1 sec to reach target, so add it in the stack 
        [[10,2,1]]
        now car at position 8 takes 1 sec to reach target with same time as the top most element of the stack, so they both reach together and their is no need to add car at position 8 also in the stack because since they both are going in same fleet, so car at position 10 will represent this fleet
        
        so again the stack become 
        [[10,2,1]]
        now car at positon 5 takes 7  sec which is more time taking than can at position 10,so we normally add it in the stack
        [[10,2,1],[5,1,7]]
        now car at position 3 takes 3 sec to reach to the target which is less time than car at position 5 which means at this rate car at position 3 will meet car at position 5 at come point of time before they both reach the target and they will start to wrok as a fleet
        so again their is no need to add car at positon 3
        [[10,2,1],[5,1,7]]
        and 
        finally car at position 0 will take 12 sec which is taking more time than car at the top of the stack so just normally append it and finally the stack becomes
        [[10,2,1],[5,1,7],[0,1,12]]
        thus the lenght of the stack is the number of fleet that will reach the end point '''
        pair =[[p, s] for p, s in zip(position,speed)]
        stack = []
        
        for p, s in sorted(pair)[-1::-1]:
            stack.append((float)(target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)