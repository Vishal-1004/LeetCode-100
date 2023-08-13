import heapq
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
#using dictionary to keep a count of frequency of the characters
#in the string
        useDict = {}
        for i in s:
            if i not in useDict:
                useDict[i] = 0
            useDict[i] += 1

#using min heap to sort the dictionary based on its characters counts
#value that is why we have inserted a tuple of (count,ch) becuase
#heap will concider count as the value to compare and sort to
#maintain a min heap
        heap = []
        for ch,count in useDict.items():
            heapq.heappush(heap,(count,ch))

        ansString = ""
#now we will keep on poping out the elments from the heap one by one
#till the heap becomes empty and we will multiply count with ch so that
#we can keep add ch for the same number of time in ansString
        while len(heap) != 0:
            count,ch = heapq.heappop(heap)
            #here we have written ansString = ch*count + ansString 
            #instead of ansString += ch*count becasue we wanted our 
            #answer in reversed order
            ansString = ch*count + ansString

        return ansString