def smallest_sums(arr1, arr2, k):

    if not arr1 or not arr2:
        return

    stack = []
    i = j = 0
    while i< len(arr1) and j < len(arr2) and k>0:
        if arr1[i] < arr2[j]:
            stack.append([arr1[i], arr2[j]])
            j+=1
        else:
            stack.append([arr1[i], arr2[j]])
            if arr1[i+1] > arr2[j+1]:
                j+=1
            else:
                i+=1
            
        k-=1
    return stack
print(smallest_sums([2,3,4,6],[1,7,11,14,15],3))
            

print(smallest_sums([1,3,11],[2,4,8],4))    
