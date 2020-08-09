def firstDup(arr):
    k = len(arr)-1
    for i in range (len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i] == arr[j]:
                k = min(k, j)
    if k == len(arr)-1:
        print ('-1')
    else:
        print (arr[k])
firstDup([2,3,2,8,3,5])


def deupFirst(arr):
    seen = set()
    for i in range (len(arr)):
        if arr[i] in seen:
            return arr[i]
        else:
            seen.add(arr[i])
    return -1
print (deupFirst([2,10,9,8,3,5]))
