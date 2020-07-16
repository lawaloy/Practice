class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        rows = m
        cols = n
        
        dp = [[1 for num in range(cols)] for num in range(rows)]

        # for row in range(rows):
        #     for col in range(cols):
        #         if row > 0 and col > 0:
        #             dp[row][col] = dp[row-1][col] + dp[row][col-1]
        #         elif row > 0:
        #             dp[row][col] = dp[row-1][col]
        #         else:
        #             dp[row][col] = dp[row][col-1]
        # return dp[rows-1][cols-1]
        
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[rows-1][cols-1]
                
            
