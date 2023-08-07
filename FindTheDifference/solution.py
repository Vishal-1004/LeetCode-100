class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        '''
        here we will be using XOR operation to solve our question. Let us understand the use of XOR with the help of an example.
        s = 'abc'
        t = 'abcd'

        now if we take XOR of every element of s then we get
        result = a^b^c
        now we will  repeat the XOR operation with every element of t we get
        result = a^b^c^a^b^c^d

        now as per XOR table 
        0^0 = 0
        1^1 = 0
        0^1 = 1
        1^0 = 1
        i.e XOR of similar elements will get cancelled out so at the end in result we will be left with 
        result = d
        Note: here we will take ASCII values of each character in the strings in concideration and perform our XOR operation 
        '''
        c = 0
        for cs in s:
            c ^= ord(cs)

        for ct in t:
            c ^= ord(ct)
        
        '''finally returning the answer by converting into character again'''
        return chr(c)