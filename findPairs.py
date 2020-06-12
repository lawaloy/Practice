def find_pairs(arr1, arr2):
    if not arr1 or not arr2:
        return []
    stack = []
    i=j=0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            stack.append([i,j])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1
    return stack
arr1, arr2 = [1,2,3,5,7,8,10,19], [2,4,6,7,10,14]
print(find_pairs(arr1, arr2))
