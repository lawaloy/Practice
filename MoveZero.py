class Solution:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def myNameAndAge(self):
        return f'my name is {self.name}, and my age is {self.age}'
data = Solution('Jide', 23)
data.age =  20
print(data.myNameAndAge())



def moveZeroes(nums):
    stack = []
    for num in range(len(nums)):
        if nums[num] != 0:
            stack.append(nums[num])
    for num in range(len(nums)):
        if nums[num] == 0:
            stack.append(nums[num])
    return stack
nums = [0,1,0,3,12]
print(moveZeroes(nums))
