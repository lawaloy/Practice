class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefixSum = []
        prefixSum = 0
        for weight in w:
            prefixSum += weight
            self.prefixSum.append(prefixSum)
        self.totalSum = prefixSum
        

    def pickIndex(self):
        """
        :rtype: int
        """
        random_num = self.totalSum * random.random()
        low, high = 0, len(self.prefixSum)-1
        while low <= high:
            mid = low + high >>1
            if random_num > self.prefixSum[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return low
                
        
