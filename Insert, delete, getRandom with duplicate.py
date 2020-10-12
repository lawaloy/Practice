import random as rand
class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._ArrayList = []
        self._orderedMap = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self._orderedMap[val].add(len(self._ArrayList))
        self._ArrayList.append(val)
        return len(self._orderedMap[val]) == 1
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self._orderedMap[val]:
            return False
        indexToUpdate = self._orderedMap[val].pop()
        valueToUpdate = self._ArrayList[-1]
        self._ArrayList[indexToUpdate] = valueToUpdate
        self._orderedMap[valueToUpdate].add(indexToUpdate)
        self._orderedMap[valueToUpdate].discard(len(self._ArrayList)-1)
   
        self._ArrayList.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        # arrayLength = len(self._ArrayList)-1
        # return self._ArrayList[random.randint(0, arrayLength)]
        return choice(self._ArrayList)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
