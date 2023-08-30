import math
class Solution:
    def minEatingSpeed(self,piles,h):
        '''at min koko will eat at the speed of 1 banana at a time and at max he will eat max(piles) banana at a times'''
        l = 1
        r = max(piles)
        '''in res we have to store min value that is why we start with r which is the max value in piles'''
        res = r 

        '''now suppose we have l = 1 and r = 11 and h = 8 and piles as [3,6,7,11]
        then we check (1+11)//2 = 6 first here
        math.ceil(3/6) = 1
        math.ceil(6/6) = 1
        math.ceil(7/6) = 2
        math.ceil(11/6) = 2
        so 1+1+2+2 = 6<8 hence for now res = 6
        now r = k-1 because we have to move to lower elements as we are expected to find min value of k 
        now l = 1 and r = 5 so k = (1+5)//2 = 3
        again doing the same we get hours as 9 which is not less than or equal to 8 so now move higher that is l = k + 1 so now l = 4 and r = 5 and new k = 4
        now eating 4 banans at a time ends up covering all the banans in time hence new res value is min(6,4) = 4 and now finally the while conditions break hence we return the res value.'''
        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1

        return res