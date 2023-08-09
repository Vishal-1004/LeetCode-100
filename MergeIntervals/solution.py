class Solution(object):
    def merge(self, intervals):
        '''created an ans array to store our final interval answer'''
        ans = []
        '''sorting the intervals array so that we can normally run a for loop and check for our conditions for preceding elements'''
        intervals.sort()

        if len(intervals) == 0:
            return ans

        '''temp is a 1D array which is initially stroing the first element form intervals array'''
        temp = intervals[0]
        '''running a for loop in intervals array'''
        for interval in intervals:
            '''now if the 1st element of the interval is less the 2nd (last element) element of the temp array then it means that the interval is overlaping with the temp array
            i.e if intervals = [[0,2],[1,4],[3,5]]
            so temp = [0,2] and interval = [1,4]
            since interval[0] = 1 < temp[1] = 2 so 
            temp[1] = max(temp[1],interval[1])
            so final temp after operationo will be [0,4] but here the point to note is that we are still not appending this temp to ans because there can be chance that the next element of intervals is also overlapping that is true for the above example [3,5] so again the changes will be made on the temp array and it will be updated as [0,5] finally when the for loop gets over we append temp in ans and shown below'''
            if interval[0] <= temp[1]:
                temp[1] = max(temp[1], interval[1])
            else:
                '''if the above condition fails that if give intervals to us was 
                [[0,2],[1,4],[5,7]]
                so here temp will be appended in ans array as [0,4] and now temp will be pointing towards [5,7] since the for gets over after this so at end its necessary for us to append temp in ans'''
                ans.append(temp)
                temp = interval
        ans.append(temp)

        return ans