class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''maxArea stores the maximum area and we have created two pointers left and right '''
        maxArea = 0
        left = 0
        right = len(height)-1

        while left < right:
            '''at first we are calculating the area and then we are compairing it with the max area
            , after every comparison we get the maximum area till the end of the loop'''
            area = min(height[left],height[right])*(right-left)

            maxArea = max(maxArea,area)
            '''now we check for the left and the right hight, if the left height is less than that of 
            right height then we increment left height else the right height is decremented'''
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea