import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        '''first we will be counting the frequency of every element in nums and keep a note of it in a dictionary'''
        countDict = {}
        for i in nums:
            if i not in countDict:
                countDict[i] = 0
            countDict[i] += 1

        '''then we will maintain a min-heap as follows'''
        heap = []
        '''running a for loop in the dictionary'''
        for num,count in countDict.items():
            '''if the lenght of the heap is less than k then we will push  the (count,num) tuple in the heap, here the heap will only concider the element at 0th index for automatic sorting of the heap where as the second element will not be concidered that is why we have kept count at 0th index while pushing the tuple in the heap'''
            if len(heap) < k:
                heapq.heappush(heap,(count,num))

                '''now if the heap's lenght is more than k then we check that the next tuple which we are going to push has more count value as compared with the count value of the tuple which is at the 0th index because at 0the index we have elements with lower count value in min heap, more over we are trying to maintain a k frequent elements so the count value must be high for the tuple to be pushed into the heap'''
            elif count > heap[0][0]:
                '''in order to push we have to first remove the top element by performing a pop operation then we can go for push operation'''
                heapq.heappop(heap)
                heapq.heappush(heap, (count,num))

        '''finally we return an array of num elements form the heap'''
        return [i[1] for i in heap]