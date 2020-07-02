import random as rand
print(rand.randint(0,12))

arr = [1,2,3,4,5,67,8,9,10,-3,-1]
i = 0
j = len(arr)-1
while i<j:
    if arr[i]%2==0:
        i+=1
    else:
        arr[i],arr[j]=arr[j],arr[i]
        j-=1
print(arr)

daa = "abode"
print(list(reversed(daa)))


def count_even(arr):
    res = 0
    for element in arr:
        res=res^element
    return res
print(count_even([1,2,3,3,4,5,1,2,4,5,7,7,7]))


