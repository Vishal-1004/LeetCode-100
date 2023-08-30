import math
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        '''here we aim to open up our matrix and store all its elments in form of a single array temp'''
        temp = []
        
        '''for every row in matrix we will extend function to store every element on every row in temp array'''
        for row in matrix:
            temp.extend(row)
        
        '''finally we will sort the array and return the required value'''
        temp.sort()
        return temp[k-1]
    
    '''
    another way of doing these kind of question can be by using heap i.e priority queue

    m = sum(matrix, [])         # convert matrix into 1D array
    heapq.heapify(m)            # heapify() to turn m into a heap
        
    for i in range(k - 1):      # pop (k - 1) elements so that we can find kth element
        #it neccessary to pop out all the k - 1 elements from the heap because heap does 
        # not behaves like an array if we try to print the heap then we will get an array 
        # all the same elements in the same order in which we tried to insert them so 
        # overcome this problem we have to pop out all the unrequired elements
        heapq.heappop(m)
            
    return heapq.heappop(m)
    '''
    '''
    import heapq

    useArr = [1,2,1,3]

    heap = []
    for i in useArr:
        heapq.heappush(heap,i)
        print(heap)

    while len(heap) != 0:
        m = heapq.heappop(heap)
        print(m)

    # here print(heap) will give the same useArr i.e [1,2,1,3] but we were expecting 
    # [1,1,2,3]. The heap will anyway be holding its property and we can verify this
    # by poping out all the elements one by one and printing it so we will get 
    # 1
    # 1
    # 2
    # 3
    # and this what we wanted
    '''