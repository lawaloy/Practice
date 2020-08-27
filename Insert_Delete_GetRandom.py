import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._arrayList = []
        self._unorderedMap = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self._unorderedMap:
            return False
        self._unorderedMap[val] = len(self._arrayList)
        self._arrayList.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._unorderedMap:
            return False
        idx = self._unorderedMap[val]
        self._arrayList[idx] = self._arrayList[-1]
        self._unorderedMap[self._arrayList[idx]] = idx
        del self._unorderedMap[val]
        self._arrayList.pop()
        return True
            
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # return choice(self._arrayList)
        return self._arrayList[random.randint(0, len(self._arrayList)-1)]
       


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
