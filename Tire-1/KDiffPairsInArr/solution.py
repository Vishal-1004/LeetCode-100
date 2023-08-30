from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        '''Counter is a method which counts the number of times an element form the array has occured in the array and gives the result in form of a dictionary where key is the elements of the array and value is the count of the respective element'''
        useDict = Counter(nums)

        '''now if the given K value is 0 then its means that the only possible way of getting 0 is that subtracting a number with the same number'''
        if k == 0:
            '''for that reason we are checking that whether the count the respective element is greater than 1 or not if yes then we increase the count by 1'''
            for key,v in useDict.items():
                if v>1:
                    count += 1

            '''if the value of K is something other than 0 then we do the following'''
        else:
            for key,v in useDict.items():
                '''for every key in useDict we add it with K and check that the resultant value is present as a key in useDict or not if yes then we increment the count by 1'''
                if key+k in useDict:
                    '''here we don't need to bother about the number of time the element has occured as its obvious that the given element would have occured atleast once and that is all what we need as we cant make duplicate pairs'''
                    count += 1

        return count