class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        '''concider some examples 
        num = 1432219 and k = 3, then what will those numbers which you will remove
        if u r thinking to remove top 3 max elements then you will get
        1221 as the out put and this is wrong
        the correct answer should be 
        1219 as < 1221
        
        now let us see how we got this answer, we wil be using monotonically increasing stack 
        that is we will allow only increasing order of elements to be appended in the stack else the element will be poped this is
        append 1 in the stack as stack is empty, we get
        [1], since 4 > 1, so the increasing order is maintained so append 4 in the stack
        we get
        [1,4], next element is 3 < 4, because of which the increasing order is not maintained so keep on poping out the top element of the stack tilll the condition statisfies, we get 
        [1,3], 2 < 3, again the increasing order is not being maintained so we keep on poping out till the conditions are maintained
        we get
        [1,2], next is 2 == 2 so append it as the order it maintained
        [1,2,2], next we have 1 < 2, the conditions failes so pop 2 and we get 
        [1,2,1], now you might why we stopped poping out then it is because we were only suppose to pop 3 elements,
        so its necessary to keep the track of k (no of elements to be poped)
        after appeding rest of the elments we get
        [1,2,1,9]
        now we have to return them as a string, so we must concider the following cases too
        
        what if the stack is empty then return "0"
        what if the stack has leading 0, then first convert the number as int and then as string and hence return it.
        '''
        stack = []

        for c in num:
            while k > 0 and stack and int(stack[-1]) > int(c):
                k -= 1
                stack.pop()

            stack.append(c)

        '''now one of the most important condition which have to check is that what if the number was 123456 and the k value was 2,
        since the number is already in ascending order so nothing will be poped out till the for loop gets over,
        and the stack we get will be
        [1,2,3,4,5,6]
        
        so to minimize the number we must remove the top most elements from the stack which are present at the right side of the stack
        so we get 1234 as our answer'''
        stack = stack[:len(stack)-k]
        res = "".join(stack)
        return str(int(res)) if res else "0"