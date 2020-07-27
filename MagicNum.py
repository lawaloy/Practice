def magic_num(num):
    
    if not num:
        return
    
    ans = []
    res = 0
    
    while num>0:
        ans.append(num%2)
        temp = num//2
        num = temp
        
    for ind in range (len(ans)):
        if ans[idx] > 0:
            res += (ans[idx] * (7**idx))
    return res

"""
N = len(ans)
Time Complexity: O(log(Num) + (N))
Space Complexity: O(N)
"""
