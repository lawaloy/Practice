def insertionSort(arr):
    for left in range (1, len(arr)):
       
        while left > 0 and arr[left-1] > arr[left]:
            arr[left], arr[left-1] = arr[left-1],arr[left]
            left-=1
    return arr
print(insertionSort([11,10,9,8,77,4,4,2,1,1,0,6,5,4,3,2,1,0]))



def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range (minIndex+1, len(arr)):
            if arr[minIndex] > arr[j]:
                arr[minIndex],arr[j] = arr[j],arr[minIndex]
    return arr
print(selectionSort([6,12,3,4,9,-2,-1]))
