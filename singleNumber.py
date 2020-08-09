def singleNum(nums):
    stack = []
    for num in range (len(nums)):
        if nums[num] in stack:
            stack.remove(nums[num])
        else:
            stack.append(nums[num])
    return stack[-1]
nums = [1,2,3,4,5,3,2,1,5]
print(singleNum(nums))
