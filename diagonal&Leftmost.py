m = [[ 1, 2, 3, 4], 
     [ 5, 6, 7, 8], 
     [ 9,10,11,12], 
     [13,14,15,16]] 

#[[1],[2,5],[3,6,9],[4,7,10,13],[8,11,14],[12,15],[16]]
def diagonalMatrix(m):
    if not m:
        return
    
    i, j = 0, len(m[0])-1
    res=[]
    for col in range(len(m[0])): #loop thru first row
        i, j  = 0, col
        diagonal = []
        while j>=0 and i < len(m):
            diagonal.append((m[i][j]))
            j-=1
            i+=1
        res.append(diagonal)
        
    # last col
    for row in range(1,len(m)): #skip the first row
        i, j = row, len(m[0])-1
        diagonalz = []
        while j>=0 and i < len(m):
            diagonalz.append((m[i][j]))
            j-=1
            i+=1
        res.append(diagonalz)
    return res
            
print(diagonalMatrix(m))



def leftMost(matrix):
    i, j, res = 0, 0, []
    min_col = 100 # left most col with 1

    while j<len(matrix[0]): #FIND FIRST 1 ON THE LEFT IN this row
        if matrix[i][j] != 1:
            j+=1
        else:
            res.append((i, j))
            min_col = j
            i+=1
            break

    while i<len(matrix) and j>=0: 
        if matrix[i][j] == 1 and j != 0 and matrix[i][j-1] == 1:
            j-=1
        else: # we are at the left most 1 of this row
            if matrix[i][j] == 1:
                if j < min_col:
                    res = [(i, j)]
                elif j == min_col:
                    res.append((i, j))
            i+=1    
    return res

#print(leftMost(m))

    
    
    
    
    
    
    
    






