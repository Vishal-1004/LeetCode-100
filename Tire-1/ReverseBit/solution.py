class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        '''variable to store the reversed number'''
        reverseNum = 0

        '''running a for loop 32 times because our number is 32 bits long'''
        for i in range(32):
            '''left shifting the reversed number by one and then doing an OR operation with the AND of n by 1. We have done AND of n with 1 so that we can get the last bit of n and then ORing it with the left shifted reverseNum will generally add the number to the end of the reverseNum'''
            reverseNum = (reverseNum << 1) | (n&1)

            '''right shifting on n by 1 will bring the second last bit of n in the last and then we can continue our above operation'''
            n >>= 1

        return reverseNum