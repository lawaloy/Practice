def wave_sort(arr):
    
    """
    I sorted the arr on the even index, except the first index,
    by comparing the value with it neighbors
    Time: O(N)
    Space: O(1)
    """
    
    if not arr:
        return
    
    for idx in range (0, len(arr), 2):
        
        
        if idx > 0 and arr[idx] > arr[idx-1]:            
            arr[idx], arr[idx-1] = arr[idx-1], arr[idx]

        if idx < len(arr)-1 and arr[idx] > arr[idx+1]:
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]

    return arr

print(wave_sort([1,2,3,4,5,6]))


            
