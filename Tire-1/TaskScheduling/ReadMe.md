# Task Scheduling

There are N tasks of varying durations, represented by an array A of size N. K workers are available, and each worker takes 1 unit of time to complete 1 unit of work. The goal is to find the minimum time required to complete all the tasks, with the constraint that each worker can only work on a continuous sequence of tasks.
To solve this problem, we can use the binary search algorithm to find the minimum time required..
e.g., with 4 tasks of 10,20,30 & 40 time duration and 2 workers, min time is 60 mins.

Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

### Method Followed
Binary Search

**Example 1**
```
Input: 
4
60 20 40 50
2
Output: 90
```
**Example 2**
```
Input:
4
10 20 30 40
2
Output: 60
```