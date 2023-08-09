class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''res array stores the final answer and intially it has null i.e [] subset of the given set nums'''
        res = [[]]
        for num in sorted(nums):
            '''now for every element in nums we add it in every array of res that is 
            initially res = [[]] and if nums = [1,2,3] then 
            for item in res means [] initially and num form nums is initially refering to 1 so for one for loop res becomes 
            [[],[1]]
            now again outer for loop's nums is now refering to 2 and 
            item in res  will refer to [] and [1] so now the res value will be
            [[],[1],[2],[1,2]] similary when num = 3 then res will be 
            [[],[1],[2],[1,2,3],[1,3],[2,3],[3]]
            thus this is what we want'''
            res += [item+[num] for item in res]
        return res
    
    ''' now suppose we would have got nums as [1,2,2] and they would have asked to find all the unique subsets so we can use the set property and the convert the res back to a list but this property only work on hashable elements and 2D array is not hashable to instead first make the inner array as tuple and then use set and list property as follows:
    unique_array = list(set(tuple(sublist) for sublist in res))'''
