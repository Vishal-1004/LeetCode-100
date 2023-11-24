def isPossible(tasks,workers,mid):
    currentWorker = 1
    currentTime = 0
    
    for i in tasks:
        currentTime += i
        if currentTime > mid:
            currentWorker += 1
            currentTime = i
            
    return currentWorker <= workers

def binarySearch(tasks,workers):
    low = max(tasks)
    high = sum(tasks)
    result = float('inf')
    
    while low <= high:
        mid = (low+high)//2
        
        if isPossible(tasks,workers,mid):
            result = min(result,mid)
            high = mid -1
        else:
            low = mid + 1
            
    return result

n = int(input())
tasks = list(map(int,input().split()))
workers = int(input())

print(binarySearch(tasks,workers))