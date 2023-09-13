class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        useArr = [i for i in range(1,n+1)]

        '''this solution is a mear implication of the explanation which is given in the example input/output field.
        here we are running a while loop till the useArr length becomes 1 and for every iteration we are poping out the first element and appending it at the back of the array. Mean while we are even keep a track of count, when this count becomes equal to k then our inner while loop breaks and then 
        we pop out the last element from the useArr as it was at the kth count and was appended back of the useArr
        
        Finally when the useArr length becomes equal to 1 we remove the last remaining element'''
        while len(useArr) > 1:
            count = 0
            while count < k:
                useArr.append(useArr.pop(0))
                count += 1
            
            useArr.pop(-1)

        return useArr[0]