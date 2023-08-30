import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        '''creating an empty max heap and pushing all the given counts of a,b and c in the heap'''
        heap = []
        '''here we have kept the count value at 0th index of each tuple because in heap it will concider only the element at 0th index for sorting'''
        if a != 0:
            heapq.heappush(heap, (-a, 'a'))
        if b != 0:
            heapq.heappush(heap, (-b, 'b'))
        if c != 0:
            heapq.heappush(heap, (-c, 'c'))

        result = ""  # -> will be storing the final answer
        '''since we have only three characters i.e a,b,c so it is obvious that we will end up having single element left in the heap, so at that point we will stop our while loop'''
        while len(heap) > 1:
            '''poping out top two elements from the heap and storing them in the respective variables'''
            count1, ch1 = heapq.heappop(heap)
            count2, ch2 = heapq.heappop(heap)

            '''since we are allowed to have substrings like aa,bb or cc so we are checking that whether the count1 value that is the max value from the heap is more than two or not'''
            if abs(count1) >= 2:
                '''if the length of the result variable is more than or equal to 2 and if the last element of result is not equal to ch1 that is if ch1 = 'a' and result till now = 'abc' so we can add 'a' two  times in result'''
                if len(result) >= 2 and result[-1] != ch1:
                    result += ch1 * 2
                    '''now if the count1 if ch1 is more than 2 we will that is 3 or more than 3 then only we will decrement the count1 value by 2 and push it back into the heap. Why we are concerned with its value being more than 2 becasue if its exactly 2 then decrementing it by 2 will make its count as 0 and we are not inserting such values in heap'''
                    if abs(count1) > 2:
                        heapq.heappush(heap, (count1 + 2, ch1))

                    '''if the lenght of result is 2 or more than 2 and if the last character of result is equal to ch1 and second last character of result is not equal to ch1 then it means we can only add ch1 once in the result'''
                elif len(result) >= 2 and result[-1] == ch1 and result[-2] != ch1:
                    result += ch1
                    '''now this time we will only check that the count1 is more than 1 or not because we have only inserte ch1 in result only once so we will be decrementing count1 by one only and push it back into the heap'''
                    if abs(count1) > 1:
                        heapq.heappush(heap, (count1 + 1, ch1))

                    '''if the lenght of result is equal to or more than 2 and if the last two characters of result are same as that of ch1 then we cannot add ch1 at the end of result as it will end up voilating rule 2 of happy strings, so we just push it back into the heap'''
                elif len(result) >= 2 and result[-1] == ch1 == result[-2]:
                        heapq.heappush(heap, (count1, ch1))

                        '''now if this is the first time we are adding something in result or the length of result is less than 2 then we just normally add ch1 twice in the result and decrement its count by 2 and push it back in the heap only if the count1 value of ch1 was more than 2'''
                else:
                    result += ch1*2
                    if abs(count1) > 2:
                        heapq.heappush(heap, (count1 + 2, ch1))

                    '''if we have count1 as 1 then we just normally add ch1 in result and their is no need for any decrement operation or anything else as if the count1 is 1 and decrementing it by 1 will lead to 0 so their's no need to add it in the heap'''
            elif abs(count1) == 1:
                result += ch1

                '''finally we add ch2 only once in the result to form patterns like aab or ccb or bba and so on because this is the only way of creating happy string of longest legth'''
            result += ch2
            if abs(count2) > 1:
                '''if the count2 value is more than 1 then we decrement its value by 1 and push it back into the heap'''
                heapq.heappush(heap, (count2 + 1, ch2))
            

            '''now if we are left with only one element in the heap then we take the count and ch value from the heap's 0th index'''
        if heap:
            count, ch = heap[0]
            '''if the length of result is more than or equla to 1 and last character of result is not equal to ch then we can add it twice in the result only if the count value is also more than or equal to 2 else we will add it only once'''
            if len(result) >= 1 and result[-1] != ch:
                if abs(count) >= 2:
                    result += ch * 2
                else:
                    result += ch

                '''if the lenght of result is 0 then just add ch in result twice if its count is more than 1'''
            elif len(result) == 0:
                if abs(count) > 1:
                    result += ch*2
                else:
                    result += ch

        '''finally we will return the result value'''
        return result