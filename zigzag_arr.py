def zigzag_arr(arr):
    if not arr:
        return arr
    bool = True
    for idx in range(len(arr)-1):
        if bool:
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            bool = False
        else:
            if arr[idx] < arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            bool = True
    return arr
arr = [4,3,7,8,6,2,1]
print(zigzag_arr(arr))
