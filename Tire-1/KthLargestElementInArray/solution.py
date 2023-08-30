import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        '''here instead of sorting we will be using min heap properties because in case of sorting the best time complexity which it can produce is of O(nlogn) and in case of heap the time complexity is O(n)
        here min heap will automatically sort the array in ascending order on its own every time an element is inserted in it. Let us try to understand this more using the following example.
        import heapq

# Creating an empty min-heap
min_heap = []

# Inserting elements into the heap
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 10)

print("Min-Heap after insertion:", min_heap)  # Output: [1, 3, 8, 5, 10]

# Getting the smallest element (root)
smallest_element = min_heap[0]
print("Smallest element:", smallest_element)  # Output: 1

# Removing the smallest element
removed_element = heapq.heappop(min_heap)
print("Removed element:", removed_element)  # Output: 1
print("Min-Heap after removal:", min_heap)  # Output: [3, 5, 8, 10]

# Convert a list into a min-heap using heapify
unordered_list = [9, 2, 7, 4, 6]
heapq.heapify(unordered_list)
print("Min-Heap after heapify:", unordered_list)  # Output: [2, 4, 7, 9, 6]

# Inserting elements and maintaining the heap property
heapq.heappush(min_heap, 2)
print("Min-Heap after insertion:", min_heap)  # Output: [2, 3, 8, 5, 10, 7]

# Removing elements and maintaining the heap property
heapq.heappop(min_heap)
print("Min-Heap after removal:", min_heap)  # Output: [3, 5, 8, 7, 10]

# Combining heaps using heapify
combined_heap = heapq.merge(min_heap, unordered_list)
print("Combined Heap:", list(combined_heap))  # Output: [2, 3, 5, 4, 7, 8, 9, 7, 6, 10]

# Using heapreplace to remove and insert an element
replaced_element = heapq.heapreplace(min_heap, 11)
print("Replaced element:", replaced_element)  # Output: 3
print("Min-Heap after replacement:", min_heap)  # Output: [5, 7, 8, 11, 10]'''

        '''here we will create a min heap and keep on inserting the elements in it and it will get automatically sorted on its own. now when ever the length of the heap goes more than k then we pop out the smallest element from the heap that is we pop out the element at 0th index and this is done by heapq.heappop method. We are doing this because we want only to maintain a heap of k largest element with element at 0th index to be the kth largest element of the array'''
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]