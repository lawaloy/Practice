def moveZero(nums):
    #does not maintain order of the array
    slow = 0
    fast = 0
    while fast < len(nums) and slow < len(nums):
        if nums[fast] == 0:
            nums[slow],nums[fast] = nums[fast], nums[slow]
            slow+=1
        fast += 1   
        #while slow< len(nums) and nums[slow] == 0:
            #slow +=1
        
    return nums
print(moveZero([0, 1,0, 1, 1, 0, 1, 1, 1, 0]))
print(moveZero([0,2,1,0,3,3,0]))
print("---------------")


def moveZeroes(arr):
    #maintain order of the array
    if not arr:
        return arr
    zero = runner = len(arr)-1

    while runner >= 0:
        if arr[runner] != 0:
            arr[runner], arr[zero] = arr[zero], arr[runner]
            zero -= 1
        runner -= 1

    return arr
print(moveZeroes([1, 1,0, 1, 1, 0, 1, 1, 1, 0]))
print(moveZeroes([0,2,1,0,3,3,0,6]))
print("---------------")

def moveZeros(arr):
    #maintain order of the array
    if not arr:
        return arr
    slow =  0

    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[fast], arr[slow] = arr[slow], arr[fast]
        if arr[slow] != 0:
            slow += 1
    return arr
print(moveZeros([1, 1,0, 1, 1, 0, 1, 1, 1, 0]))
print(moveZeros([0,2,1,0,3,3,0,6]))

   
