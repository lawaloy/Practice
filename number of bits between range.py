def number_of_bit(n):
    count = 0
    ans = [0]*(n+1)
    for i in range (1, n+1):
        ans[i]= ans[i>>1] + (i&1)
    for k in ans:
        count+=k
    return count
n = 8
print(number_of_bit(n))
#calculate number of bit between range
