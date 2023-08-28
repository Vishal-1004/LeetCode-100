class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        hamming distance means
        1   (0 0 0 1)
        4   (0 1 0 0)
                ↑   ↑
        The above arrows point to positions where the corresponding bits are different.

        now in order to find hamming distance between all the pairs let us consider the following example
        14      1 1 1 0
        2       0 0 1 0
        4       0 1 0 0

        here at first bit (from right) 
        no of Zeros = 3 and
        no of Ones = 0
        so hamming distance will be 0*3 = 0 cause their is no set bit

        now for second bit (from right)
        no of Zeros = 1 and
        no of Ones = 2
        so hamming distance will be 1*2 = 2, because with one 0 it can form pair with any of the available two 1s.
        And this way we will be able to address all the pairs in tha array and finally we will get the answer
        '''
        ans = 0
        for i in range(32):
            zero = one = 0
            mask = 1 << i
            '''with the help of mask we are keeping the count of one and zero'''
            for num in nums:
                if mask & num:
                    one += 1
                else:
                    zero += 1

            ans += one*zero

        return ans