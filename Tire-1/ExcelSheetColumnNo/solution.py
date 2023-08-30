class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        useDict = {
                    'A': 1,  'B': 2,  'C': 3,  'D': 4,  'E': 5,  'F': 6,
                    'G': 7,  'H': 8,  'I': 9,  'J': 10, 'K': 11, 'L': 12,
                    'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                    'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
                    'Y': 25, 'Z': 26
                }       
        '''Let us try to understand our methond with the help of an example
        AB = 1*26^1 + 2*26^0, like wise
        AAA = 1*26^2 + 1*26^1 + 1*26^0
        from this you would have clearly understood that we will be maintaing a radix with initial value as 0 and will keep on incrementing its value by 1. This methond of ours is same as finding the numbers values based on their ones,thens,hundres positions. The only difference is that here we are using 26 because we have 26 alphabets.
        '''
        radix = 0
        ans = 0
        for i in columnTitle[-1::-1]:
            ans += useDict[i]*(26**radix)
            radix += 1

        return ans