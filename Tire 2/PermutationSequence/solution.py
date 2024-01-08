import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        '''
        if u look at the permutation of 3 after arranging them in order you will get
                123  213  312
                132  231  321
        index =  0    1    2
        as you can see over here that the numbers are arranged in three different blocks
        and now if we are suppose to find out the value at k = 5 then we will be looking at 3rd block that is 2nd index and we get this by using the formula
        index = ceiling value of(k / (n-1)!)

        now their is an exception to it that is if they ask us to find the value at k = 4
        then according to our formula
        index = 4/2! = 2nd index but our correct answer is at index 1

        so when ever k % (n-1)! == 0  then we reduce index value by 1 always

        now moving forward we will also have an array which will have all the elements already written in it in increasing order that is
        [1,2,3]
        here at index 2 we have "3" so add it in our "ans" variable and also remove it from the array, so now we have [1,2] in left in the array because we are currently left to decided the position for 1 and 2 only.

        now update the k value by using the formula newK = k - (n-1)! * index
        here for the above example we are getting newK = 5 - 2*2 = 1

        now repeate the same steps again using k as 1 and newArray as [1,2] and now the blocks are as follows
                  312  321
        index =    0    1
        here again using the formula we will get
        index = ceiling of(k / (n-1)!) = 1 / (2-1)! = 1
        and again k % (n-1)! == 0 so index -= 1 => index = 0

        thus from the array at index 0 we have 1 so "ans" gets updated to "31" and so on...

        '''
        digit = [i for i in range(1,n+1)]

        def function(digit,k,n,ans):
            factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
            if len(digit) == 0:
                return ans

            index = int(math.ceil(k/factorial[n-1]))
            #print(index)
            if k % factorial[n-1] == 0:
                index -= 1

            ans += str(digit[index])
            #print(ans,index,digit)
            digit.pop(index)
            return function(digit,k - factorial[n-1]*index,n-1,ans)

        return function(digit,k,n,"")
