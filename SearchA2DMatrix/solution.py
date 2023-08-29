class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''first we keep a note of ROWS and COLS of the matrix'''
        ROWS,COLS = len(matrix),len(matrix[0])

        '''now we will first try to find out that exactly in which row does our traget value can below to. For this we are going to apply binary seach on the ROWS of the matrix. Here top and bot represents the top and bottom ROWS of the matrix'''
        top,bot = 0,ROWS-1
        while top<=bot:
            row = (top+bot)/2
            '''if the target is gerater than the last element of the current row then we can say that we must look in more higher rows that is why we do top = row+1'''
            if target > matrix[row][-1]:
                top = row + 1
                '''if the target is less than the first element of the given row then we have to look lower that is why we do bot=row-1'''
            elif target < matrix[row][0]:
                bot = row - 1
            
                '''else we would have find the the exact row in which our element should belong so we break over here'''
            else:
                break
        
        '''their can be a chance that the while loop would have broken due to the failer of its condition that is top<=bot, if that's the case then we must check it and return False cause it indicates that their is no such row which would contain our target'''
        if not(top<=bot):
            return False

        '''other wise perform binary search again in the given row of the matrix and return the answer accodingly'''
        row = (top+bot)//2
        l,r = 0,COLS-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False