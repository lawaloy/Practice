Class DSU:
    
    def __init__(self, nums):

        self.data = [idx for idx in range(len(data))]

    def find(data, i):
        if i != data[i]:
            data[i] = find(data, data[i])
        return data[i]
    def union(data, i, j):
        pi, pj = find(data, i), find(data, j)
        if pi != pj:
            data[pi] = pj
    def connected(data, i, j):
        return find(data, i) == find(data, j)

#where nums = len(self.data)
