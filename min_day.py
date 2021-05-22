def min_day(A, N):
    include = A[0]
    exclude = 0

    for i in range (1, N):
        add_day = A[i] + min(include, exclude)
        remove_day = include

        include = add_day
        exclude = remove_day
    return min(include, exclude)
print(min_day([1,1,1,1,1],5))
