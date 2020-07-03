class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
#         if n <= 1:
#             return 1
        
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
        
#         for num in range (2, n+1):
#             dp[num] = dp[num-1] + dp[num-2]
            
#         return dp[n]

#OR
                
        if n <= 1:
            return 1
    
        first, second = 1, 1,
        
        for num in range(2, n+1):
            third = first + second
            first = second
            second = third
            
        return second
            
        #can take 1,2, or 3steps
        # first, second, third = 1,1,2
        # for num in range(2, n):
        #     fourth = first + second + third 
        #     first = second   
        #     second = third   
        #     third = fourth  
        # return third

        
