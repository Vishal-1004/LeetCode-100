class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '''if length of s is shorter than 10 then return an empty array'''
        if len(s) <= 10:
            return []

        '''variables to store the final answers'''
        ansDict = {}
        resArr = []

        '''giving specific codes to the characters so that we can use them to find our total value'''
        code = {'A':1,'C':2,'G':3,'T':4}

        value = 0
        base = 10

        '''finding the initial value of first 10 characters'''
        for i in range(10):
            value *= base
            value += code[s[i]]

        '''so for the given value we will initiate the count as 1 in ansDict'''
        ansDict[value] = 1

        '''now we will start our while loop from index 1 because we have already calculated 
        for index 0 to 9'''
        l = 1
        while l + 9 < len(s):
            '''finding out the left and right elements and there codes'''
            leftCharCode = code[s[l-1]]
            rightCharCode = code[s[l+9]]

            '''subtracting leftCharCode X 10^9 from value and then multiplying value with base and finally adding rightCharCode in it'''
            value = value - (leftCharCode*(base**9))
            value *= base
            value += rightCharCode

            '''modifying the ansDict accordingly'''
            if value in ansDict:
                ansDict[value] += 1
            else:
                ansDict[value] = 1

            '''if any key's value becomes equal to 2 then it should be added to our resArr'''
            if ansDict[value] == 2:
                resArr.append(s[l:l+10])

            '''don't forget to keep on incrementing l by one so that we can keep moving forward'''
            l += 1
            
        return resArr