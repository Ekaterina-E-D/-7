def rcr(a):
    res = [a[-1]]
    res += a[:n-1]
    return res
 
n = int(input('n = '))
lst = [x for x in input().split()]
print(*rcr(lst))