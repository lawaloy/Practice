def longest_substring_withK_distinct(arr, k):
    if len(arr) <= k:
        return len(arr)
    maxLength = curLength = windowStart = 0
    hashMap = {}

    for windowEnd in range(len(arr)):
        rightSide = arr[windowEnd]
        hashMap[rightSide] = hashMap.get(rightSide, 0)+1

        while len(hashMap) > k:
            leftSide = arr[windowStart]
            hashMap[leftSide] -= 1
            if hashMap[leftSide] == 0:
                del hashMap[leftSide]
            windowStart += 1
        curLength = (windowEnd - windowStart) +1
        maxLength = max(maxLength, curLength)
    return maxLength
arr = "cbboioioilkjhytgfdewasdfghj"
k = 2
print(longest_substring_withK_distinct(arr, k))
