class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        '''cars on left side which are moving in left direction are never going to collide,
        Similarly, cars on right side which are moving right side are never going to collide 
        In between them every car is going to collide.If they are not satable i.e 'S'.
        concider the following example 
        LLRLSLRRR ---> here we will first filter out the left and right moving cars at the prefix and suffix of the string, we get
        RLSL
        now at index 0 we have R which is not equla to S so it will collide hence count+=1 next at index 1 we have L which is not equal to S so it will collide hence count+=1
        
        you might doubt this so look below
        if after R we would have had S still collision would have occured and if would have had L then also collision would have occured '''
        left = 0
        right = len(directions) - 1

        while left < len(directions) and directions[left] == 'L':
            left += 1

        while right >= 0 and directions[right] == 'R':
            right -= 1

        count = 0
        for i in range(left,right+1):
            if directions[i] != 'S':
                count += 1

        return count