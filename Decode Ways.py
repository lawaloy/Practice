class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        count1 = count2 = 1
        for num in range(1, len(s)):
            firstNum = int(s[num])
            secondNum = int(s[num-1]) *10 +firstNum
            
            count = 0
            if firstNum > 0:
                count += count1
            if 10 <= secondNum <= 26:
                count += count2
            count2 = count1
            count1 = count
        return count
