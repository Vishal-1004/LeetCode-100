class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        '''here we will be checking for the following conditions 
        if the number of open parenthesis in the ans string is less than n then we add more of it
        if the number of close parenthesis in the ans string is less than number of open parenthesis then we add more of it
        if no. of open parenthesis is equal to no. of close parenthesis then we just add our ans string to the result array 
        
        now let us see the reason for doing all this:
        intially we have an empty stack
        []
        now we can make only one choise that is we can only add ( because openN > closeN and openN < n, so  we get
        [(]
        now we can either add ( or ) becasue our conditions are satisfied, so we get
        [((] and [()]
        now 
        [((]
         | \ 
         |  \ 
         |   \ 
         |    \ 
        [(((]  [(()]
         |        |  \ 
         |        |   \ 
        [((()]    |    \ 
         |      [(()(]  [(())]
         |         |        \ 
        [((())]    |         \ 
         |        [(())()]    [(())(] 
         |                      |
         |                      |
         |                    [(())()]
        [((()))] 
        so as you can see we have been following our conditions as trying to implement it and once openN == closedN == n we get our final generated parenthesis 
        which can be added in the result array
        like wise we can demonstrate this for [()] also'''
        stack = []
        res = []

        def backtrack(openN,closedN):
            '''if all of them are equal then we got our answer'''
            if openN == closedN == n:
                res.append("".join(stack))

            '''if openN is less than n then it means we can add some more of ( in the stack 
            and with this we call the backtrack function again with updated openN value and once done we pop out the open parenthesis i.e ( which we added earlier'''
            if openN < n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()

            '''if closedN is less than openN it means we add more of closed parenthesis in the stack and procede accoringly'''
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return res