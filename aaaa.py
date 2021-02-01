def all_bst_preorders(n):
    class Node: 
        def __init__(self , item): 
            self.key = item 
            self.left = None
            self.right = None
  
    def preorder(root): 
        if root is not None: 
            print(root.key,end=' '), 
            preorder(root.left) 
            preorder(root.right) 
    
    
    def getTrees(arr , start , end): 
    
        # List to store all possible trees 
        trees = []  
        
        if start > end : 
            trees.append(None) 
            return trees 
        
        for i in range(start , end+1):
            # Constructing left subtree 
            ltrees = getTrees(arr , start , i-1)
            # Constructing right subtree 
            rtrees = getTrees(arr , i+1 , end)

            for j in ltrees: 
                for k in rtrees:
                    node  = Node(arr[i])
                    node.left = j
                    node.right = k
                    trees.append(node)
        return trees 

    trees = getTrees(list(range(1,n+1)) , 0 , n-1) 
    for i in trees : 
        preorder(i);
        print()

size = int(input())
all_bst_preorders(size)
