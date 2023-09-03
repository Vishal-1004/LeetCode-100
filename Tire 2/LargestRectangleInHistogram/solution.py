class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''
        |
        |         6
        |      5 |``|
        |     |``|  |
        |     |  |  |   3
        |2    |  |  |2 |``|
        |``|1 |  |  |``|  |
        |  |``|  |  |  |  |
        __.__.__.__.__.__.

        here in our stack we will have the track of both the index and the height.
        initially the stack is empty so we just normally add it in the stack that is (0,2)

        next we have 1 to be added in the stack, so now sice 2 cannot continue moving in right side so we just pop it out after calculating its current height that is
        Area = height * (currentIndex - indexOf2)
        Area = 2*(1-0) = 2

        we will update the maxArea accordingly
        and 1 will be added to the stack but with the starting index of 2 cause 1 can be stretched from the start of 2 to its current index till now 
        so in stack we add (0,1)

        next we have 5, since 5>1 so we normally add in the stack that is (2,5)
        next we have 6, since 6>5 so we normally add in the stack that is (3,6)

        now we get 2 to be added, so since 2<6 that means that 6 cannot move further so we need to pop it after finding its area so
        area = 6*(4-3) = 6, update maxArea

        now we get 5, again 5<2 so we will pop it after finding its area that is
        area = 5*(4-2) i.e height*(currentInde - indexOf5) = 10, update maxArea

        now we get 1<2 so we stop here and now we will append 2 in the stack with the start index as index of 5 that is 2
        so (2,2) is added in the stack 

        now we get 3, since 3>2 we normally add it in the stack that is (5,3)

        finally the input heights array get over, but since we are still left with few elements in the stack we will have to find their areas too
        we are left with (0,1),(2,2),(5,3) so their area will be
        areaOf3 = height*(len(heights)-indexOf3)
        cause 1,2,3 where the elements which were able to stretch till the end of the array

        finally we get the answer 10 as our maxArea
        '''
        maxArea = 0
        stack = [] #pair: (index,height)

        for i,h in enumerate(heights):
            start = i
            '''as you can see here we keep on poping till the stack get empty of till the last element of the stack is greater than current height'''
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea,height*(i-index))
                '''stact keeps on shifting backwards as we pop, because that is going to be our new index of the current element'''
                start = index
            stack.append((start,h))

        '''calculating the areas for the left out elements'''
        for i, h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))

        '''finally returning the maxArea'''
        return maxArea