class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        Number of good way to split a string
        """
        result = 0
        
        if not s:
            return 0
        
        leftSideMap = {}
        rightSideMap = {}
        sList = [0] * len(s)
        
        for idx in range(len(s)):
            curChar = s[idx]
            if curChar in leftSideMap:
                sList[idx] = sList[idx-1]
            else:
                leftSideMap[curChar] = leftSideMap.get(curChar, 0) +1
                sList[idx] = sList[idx-1]+1
                
        uniqueChar = 0
        for idx in range(len(s)-1, 0,-1):
            
            if s[idx] not in rightSideMap:
                uniqueChar += 1
                rightSideMap[s[idx]] = uniqueChar
            if sList[idx-1] == uniqueChar:
                result +=1 
        return result
