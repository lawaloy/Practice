def moveZero(nums):
    slow = 0
    fast = 1
    while fast < len(nums) and slow < len(nums):
        if nums[fast] == 0:
            nums[slow],nums[fast] = nums[fast], nums[slow]
            slow+=1
        fast +=1
        # while slow< len(nums) and nums[slow] == 0:
        #     slow +=1
        # fast+=1
    return nums
print(moveZero([1, 1, 1, 1, 1, 1, 1, 0]))