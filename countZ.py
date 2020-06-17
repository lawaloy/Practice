def count_zero(nums):
    if not nums:
        return 0
    count= row = col = 0
    rowLen = len(nums)
    colLen = len(nums[0])-1

    while row < rowLen and colLen >= 0:
        if nums[row][colLen] == 1:
            colLen -= 1
        else:
            count += colLen +1
            row += 1
    return count
print(count_zero([[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1]]))
