You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations

Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:  
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        
        if len(s) <= 1:
            return s
        
        strLen = len(s)
        leftShift = rightShift = 0
        
        for direction, amount in shift:
            if direction == 0:
                leftShift += amount
            else:
                rightShift += amount
        
        sum = (leftShift - rightShift) % strLen
        # if sum > 0:
        #     return s[sum:] + s[:sum]
        # # elif sum < 0:
        # #     return s[:sum] + s[sum:]
        # else:
        #     return s
        return s[sum:] + s[:sum]
