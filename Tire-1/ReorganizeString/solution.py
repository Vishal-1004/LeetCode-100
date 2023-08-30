import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''here our main idea is to first count the frequencies of each character in the string and keeping a note of it in dictionary and then we will be using max heap to store then
        max heap is same as that of min heap the only difference is that here we store the count value in negative manner that is if we have an array of count as [10,2,13,4]
        then in normal heap it well get stored as [2,4,10,13] but we store there value in negative manner then we get [-13,-10,-4,-2] this is how max heap is constructed
        '''
        countDict = {}
        for i in s:
            if i not in countDict:
                countDict[i] = 0
            countDict[i] += 1

        heap = []
        for ch,count in countDict.items():
            heapq.heappush(heap,(-count,ch))

        '''by this line we will be having a heap like [(-3,'a'),(-2,'b')....] now what we are going to do is that we will be poping top two elements at a time form the heap and will append it in the result string in same order. now only if the frequency of poped elements is more than 1 we decrement its value and push it back into to max heap and if the frequency is 1 we don't decrement its value and push it back into  the max heap cause their is no meaning of storing those chracters of the string whose frequency is reduced to zero.'''
        result = ""
        while len(heap) > 1:
            '''one thing to be noted is that here we are running a for loop till we have at least two elements in the heap if the length of the heap becomes 1 the while loop breaks, this conditions is set for all the odd length of strings because here we are always poping out two elements at a time so it is necessary for the heap to be of length 2 atleast'''
            f1,c1 = heapq.heappop(heap)
            f2,c2 = heapq.heappop(heap)

            result += (c1+c2)

            if abs(f1) > 1:
                heapq.heappush(heap,(f1+1,c1))
            if abs(f2) > 1:
                heapq.heappush(heap,(f2+1,c2))

        if heap:
            '''now if the string length is odd then we will have one single element at teh end in the heap we will take that value and check that wether its frequency is more than one or not. If it is more than one then we return and empty string casue we cannot repeat any character and if its 1 then we just add that character at the end of the result string and return it'''
            f,c = heap[0]
            if abs(f) > 1:
                return ""
            else:
                result += c

        return result

            