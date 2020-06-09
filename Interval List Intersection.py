def intersect_ion(A, B):
    if not A or not B:
        return []
    result = []
    first = second = 0
    
        
    while first < len(A) and second < len(B):
        temp = [0] * 2
        if  B[second][1] >= A[first][0] and A[first][1] >= B[second][0]:
            temp[0] = max(A[first][0], B[second][0])
            temp[1] = min(A[first][1], B[second][1])
            result.append(temp)

        if A[first][1] < B[second][1]:
            first += 1
        else:
            second += 1
    return result
print(intersect_ion([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]]))