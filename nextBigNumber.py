class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # last_val = -1
        # for val in range (len(arr)-1,-1,-1):
        #     last_val,arr[val] = max(arr[val], last_val),last_val
        # return arr
        
        #Or
    
        # right_max = arr[-1]
        # for char in range(len(arr)-2,-1,-1):
        #     temp, arr[char] = arr[char], right_max
        #     if temp > right_max:
        #         right_max = temp
        # arr[-1]=-1
        # return arr


        #Or
        
        element = arr[-1]
        for i in range (len(arr)-2, -1, -1):
            if arr[i] > element:
                element, arr[i] = arr[i], element
            else:
                arr[i] = element
        arr[-1] = -1
        return arr
