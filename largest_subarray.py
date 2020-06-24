def largest_subarray(arr, k):
    if not arr and not k:
        return [ ]
    if not arr or not k:
        return [ ]
    if len(arr) < k:
        return [ ]
    if len(arr) == k:
        return arr
    maxSum = float('-inf')
    curSum = windowStart = 0
    result = [ ]
    for windowEnd in range (len(arr)):
        curSum += arr[windowEnd]

        if windowEnd >= k-1:
            if curSum > maxSum:
                maxSum = curSum
                result = arr[windowStart : windowEnd+1]
            curSum -= arr[windowStart]
            windowStart += 1

    return result
print(largest_subarray([9,1,2,8,7,6,5], 4))

