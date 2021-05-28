def maximumSum(arr):
    if not arr:
        return 0
    inc = arr[0]
    exc = 0

    for idx in range(1, len(arr)):
        curNum = arr[idx]
        inc_new = max(curNum+exc, inc)
        exc = inc
        inc = inc_new

    return max(exc, inc)
arr = [5,5,10,100,10,5]
arr1 = [10,5,2,7,10]
print(maximumSum(arr1))

def minimumSum(arr):
    if not arr:
        return 0
    inc = arr[0]
    exc = 0

    for idx in range(1, len(arr)):
        curNum = arr[idx]
        inc_new = curNum + min(exc, inc)
        exc = inc
        inc = inc_new

    return min(exc, inc)

arr = [5,5,10,100,10,5]
arr1 = [10,5,7,10]
arr2 = [10,5,2,4,8,6,7,10]
print(minimumSum(arr1))
