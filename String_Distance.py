def deletionDistance(str1, str2):
    str1Len = len(str1)
    str2Len = len(str2)
    
    # allocate a 2D array with str1Len + 1 rows and str2Len + 1 columns
    memo = [[0 for col in range(str2Len+1)] for row in range(str1Len+1)]

    for i in range(str1Len+1):
        for j in range(str2Len+1):
            if (i == 0):
                memo[i][j] = j
            elif (j == 0):
                memo[i][j] = i
            elif (str1[i-1] == str2[j-1]):
                memo[i][j] = memo[i-1][j-1]
            else:
                memo[i][j] = 1 + min(memo[i-1][j], memo[i][j-1])

    return memo[str1Len][str2Len]

    """
    Time Complexity: O(len(str1) *len(str2))
    Space Complexity: O(len(str1) * len(str2))
    """