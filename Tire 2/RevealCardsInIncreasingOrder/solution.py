'''
Intuition
Given to us is a deck of numbers which can be in any order.
We are suppose to give an order which follows the following rule:
From the given deck remove the first element and reveal it.
Then take the next element and append it back to the deck.
Continue doing this in such a way that the cards which are revealed are in ascending order.
For this we will be maintaining two extra arrays:
a queue which will contain all the index starting from 0 to len(deck)-1
an ansArr which will contain our correct order and we are suppose to return it at the end.
Now let us try to understand the approach with an example.
Approach
concider the deck as [17,13,11,2,3,5,7].

sort the given deck, we get: [2,3,5,7,11,13,17].

create a queue which contains all the index starting from 0 to len(deck)-1:
queue = [0,1,2,3,4,5,6]

create an ansArr which will be containing our answer:
ansArr = [0]*len(deck)

now run a for loop, that is
for i in deck:

now what ever index is at the top of queue, at that index we will append the ith element of the deck and then we will pop out that top index from the queue.

then the next element has to be poped and pushed back in the queue only if the length of the queue is >= 1.

Let us try to under stand this with an example:
deck = [17,13,11,2,3,5,7]
sorted(deck) = [2,3,5,7,11,13,17]
ansArr = [0,0,0,0,0,0,0]
queue = [0,1,2,3,4,5,6]

now i = 0
so at index 0 (top index in queue) put ith element of the deck
we get
ansArr = [2,0,0,0,0,0,0]

perform popleft on the queue
now queue becomes:
queue = [1,2,3,4,5,6]
now popleft the index of queue and append it back of the queue, we get
queue = [2,3,4,5,6,1]

now i = 1
so at index 2 (top index in queue) put ith element of the deck, we get
ansArr = [2,0,3,0,0,0,0]

perform popleft on the queue we get
queue = [3,4,5,6,1]
and now popleft the index of queue and append it back of the queue, we get
queue = [4,5,6,1,3]

continue the same and our ansArr & queue will go in the following order:
ansArr
[0,0,0,0,0,0,0] -> intially
[2,0,0,0,0,0,0]
[2,0,3,0,0,0,0]
[2,0,3,0,5,0,0]
[2,0,3,0,5,0,7]
[2,13,3,0,5,0,7]
[2,13,3,11,5,0,7]
[2,13,3,11,5,17,7]

queue
[0,1,2,3,4,5,6] -> intially, 2 goes at index 0
[2,3,4,5,6,1] -> 3 goes at index 2
[4,5,6,1,3] -> 5 goes at index 4
[6,1,3,5] -> 7 goes at index 6
[3,5,1] -> 11 goes at index 3
[1,5] -> 13 goes at index 1
[5] -> 17 goes at index 5
'''
from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)
            
        #print(queue)
        ansArr = [0]*len(deck)
        for i in sorted(deck):
            ansArr[queue[0]] = i
            queue.popleft()
            if queue:
#in case of above example we had [5] at the end which gets
#poped in the above step and now nothing is left in the queue in
#that case we have to avoid this below step that is why we have 
#this if statement
                queue.append(queue.popleft())
            #print(queue)
            #print(ansArr)
        
        return ansArr