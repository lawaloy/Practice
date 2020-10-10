def mutateTheArray(n, a):
    if not  a:
        return[]
    b = [0]* len(a)
    for num in range(n):
        if num-1 < 0:
            b[num] = 0 + a[num] + a[num+1]
        elif num+1 >= n:
            b[num] = a[num-1]+a[num]+0
        else:
            b[num] = a[num-1] + a[num] + a[num+1]
    return b

print (mutateTheArray(5, [4, 0, 1, -2, 3]))

