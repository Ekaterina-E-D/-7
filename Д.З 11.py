N=int(input("Введите количество элементов списка "))
res=[]
for i in range(N): 
    a=int(input())
    res.append(a)
res_reverse=list(reversed(res))
print(res_reverse)