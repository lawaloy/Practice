def findMaxConsecutiveOnes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    cur = maxOne = 0
        
    for num in nums:
        if num == 1:
            cur += 1
        else:
            if cur > maxOne:
                maxOne = cur
            cur = 0
    return max(maxOne, cur)