# Contiguous Array

Given a binary array 'nums', you are required to find the maximum length of a contiguous subarray that contains an equal number of 0s and 1s.

### Method Followed
Prefix Sum

**Example 1**
```
Input: nums = [0, 1, 0]
Output: 2
Explanation: The longest contiguous subarray with an equal number of 0s and 1s is either [0, 1] or [1, 0], both with a length of 2.
```
**Example 2**
```
Input: nums = [0, 0, 0, 1, 1, 1]
Output: 6
Explanation: The longest contiguous subarray with an equal number of 0s and 1s is [0, 0, 0, 1, 1, 1] with a length of 6.
```