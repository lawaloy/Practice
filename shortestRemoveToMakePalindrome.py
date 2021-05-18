def shortestRemoveToMakePalindrome(s):
    rows = cols = len(s)
    

    dp = [[0 for _ in range(cols)] for _ in range(rows)]

    for row in range(rows-1, -1, -1):
        for col in range(row+1, cols):
            if s[row] == s[col]:
                dp[row][col] = dp[row+1][col-1]
            else:
                dp[row][col] = min(dp[row+1][col], dp[row][col-1])+1

    return dp[0][-1]

print(shortestRemoveToMakePalindrome("ababa"))
print(shortestRemoveToMakePalindrome("abcdba"))
print(shortestRemoveToMakePalindrome("aebcbda"))
