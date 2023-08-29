class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0

        '''here we will be running a for loop till any one of the number becomes less than 0.'''
        while a>0 or b>0 or c>0:
            '''we will collect the last bits of each number in the respective variables'''
            lastA = a&1
            lastB = b&1
            lastC = c&1

            '''if lastC == 0 and lastA OR lastB == 1 then the possibilities are that either both lastA and lastB are 1 or any one of them is one so based on that we either add 2 to count or 1 to count respectively'''
            if lastC == 0 and lastA|lastB != 0:
                if lastA == lastB == 1:
                    count += 2
                else:
                    count += 1

            '''if lastC == 1 and lastA OR lastB == 0 then any one of lastA or lastB is needed to be changed, so we increment count value by one only'''
            if lastC == 1 and lastA|lastB != 1:
                count += 1

            '''finally right shifting all the values by one so that the while loop could terminate accodingly'''
            a = a>>1
            b = b>>1
            c = c>>1


        return count