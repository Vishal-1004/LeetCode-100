'''
[0, 0, 0, 1, 1, 1, 1, 0]
nums = [-1, -1, -1, 1, 1, 1, 1, -1]
prefix_sum = [0, -1, -2, -3, -2, -1, 0, -1, 0]
indexing ->   0   1   2   3   4   5  6   7  8

here we are concerned about the repeated values which have appeared again and again. Because it shows that these sub set contains equal number of 0s and 1s.
so as you can see we have 3 - 0s at indexes 0, 6 and 8, so we can create subarry of length max of 8 which will have equal number of 0s and 1s

like wise -1 appears 3 times at indexes 1, 5 and 7, so max sub array of length 6 can be created which will have equal number of 0s and 1s.

based on this idea we have written a code below 
'''
def findMaxLength(nums):
    # Replace 0s with -1
    nums = [-1 if num == 0 else 1 for num in nums]

    # Create a prefix sum array
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # Create a dictionary to store the first occurrence of each sum
    sum_dict = {}
    max_length = 0

    for i in range(len(prefix_sum)):
        if prefix_sum[i] in sum_dict:
            # Update the maximum length if the sum is already in the dictionary
            max_length = max(max_length, i - sum_dict[prefix_sum[i]])
        else:
            # Store the first occurrence of the sum
            sum_dict[prefix_sum[i]] = i

    return max_length

# Test cases
nums1 = [0, 1]
print(findMaxLength(nums1))  # Output: 2

nums2 = [0, 1, 0]
print(findMaxLength(nums2))  # Output: 2

nums3 = [0, 0, 0, 1, 1, 1]
print(findMaxLength(nums3))  # Output: 6

nums4 = [0, 0, 0, 1, 1, 1, 1, 0]
print(findMaxLength(nums4))  # Output: 8
