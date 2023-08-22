class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        '''here we will be using an array of all of the english alpha. to find our column title. We will on dividing the given columnNumber with 26 and what ever the remainder we get based on that value we must add the char from the array in the final ans string and then we will update the columnNumber value as the quoteint which we got on dividing columnNumber with 26'''

        useArr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',   'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        ansStr = ""
        while columnNumber > 0:
            '''here we are using columnNumber - 1 so that we can get our number range from 0 to 25 so that their could be no problem with the array indexing'''
            ansStr = useArr[(columnNumber-1)%26] + ansStr
            columnNumber = (columnNumber-1)//26

        return ansStr