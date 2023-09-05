class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        '''in order to understand our solution let us concider an example
        temperatures = [73,74,75,71,69,72,76,73]
        here we will be using monotonic stack to solve this question, 
        monotonic stack is nothing but a stack of decreasing order that is it contains all the elements in decresing order, hence its left most element is the gretest element let us maintain such a stack
        stack = []
        if the stack is empty append 73 in it
        [73], now next element in the given array is 74 and since 74 is greater than the top most element of the stack that is 73 so we pop 73 and put 74 in place of it
        [74] and marks 74 as the next nearest greater element for 73
        now next element in the array temperatures is 75 we repeat the same and now stack becomes
        [75]
        next element is 71, now since 71 is less than 75 so we just normally add it in the stack, we get
        [75,71] same goes for 69, we get
        [75,71,69], now next element is 72 since it is greater than 69 and 71 so we pop out these two elements from the array and mark 72 as the next nearest greatest element of 69 and 71,  stack becomes
        [75,72]
        now we add 76, since 76 > 72 and 76 > 75, so we pop out all these elements and mark 76 is as their next nearest greates element and now the stack becomes 
        [76] and finally 73 is also added in the stack

        this is now monotonic stack works. Concidering the same idea in mind we are going to write our code
        '''

        '''result array is intiallised with 0, so even if their is no temperature rise for a given temperature it will be already set as 0 only.'''
        res = [0]*len(temperatures)
        '''in stack we intend to store [temperature, indexOfThatTemperature]
        we will use this index to find the number of days after which we get a warmer temperature.'''
        stack = [] #pair: [temp,index]


        for i, t in enumerate(temperatures):
            '''while the stack is alive and the new temperature which we are going to add in the stack is greater than the top most element of the stack, we pop out the top most element and for this poped element the rise in temperature is caused due to this new element which is going to be added so we find their index difference and update out res array accoridingly'''
            while stack and t > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            
            '''finally the new temperature is added to the stack along with its index'''
            stack.append([t,i])

        return res