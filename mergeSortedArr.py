def mergeSortedArr(arr1, arr2):

    if not arr1 and not arr2:
        return arr1
    if not arr2:
        return arr1
    if not arr1:
        return arr2
    if arr1[0] < arr2[0]:
        return [arr1[0]] + mergeSortedArr(arr1[1:], arr2)
    else:
        return [arr2[0]] + mergeSortedArr(arr1, arr2[1:])

print(mergeSortedArr([1,2,32,52,300,1000], [0,10,11,90,900]))
