def checkifExist(arr):
    if not arr:
        return False

    seen = set()
    for nums in arr:
        if nums*2 in seen:
            return True
        elif nums % 2 == 0 and nums/2 in seen:
            return True
        else:
            seen.add(nums)
    return False
arr = [3,7,2,5,1]
print(checkifExist(arr))
