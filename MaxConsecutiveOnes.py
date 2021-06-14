def maxIndexAndCountZero(arr):
    
    maxIdx = None
    prev, prevPrev = 0, -1
    maxCount = 0

    for idx in range(len(arr)):
        if arr[idx] == 0:
            curMax = idx - prevPrev
            if curMax > maxCount:
                maxCount = curMax
                maxIdx = prev
            prevPrev = prev
            prev = idx

    if len(arr) - prevPrev > maxCount:
        maxIdx = prev
    return maxIdx, maxCount

print(maxIndexAndCountZero([1,1,0,0,1,0,1,1,1,0,1,1,1]))
print(maxIndexAndCountZero([0]))
print(maxIndexAndCountZero([0,0]))
print(maxIndexAndCountZero([0,0,1,0,1,1,1,0,1,1]))
print(maxIndexAndCountZero([0,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1]))
