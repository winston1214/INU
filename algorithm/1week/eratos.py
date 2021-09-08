def eratos(a,n):
    a[1] = 0
    i = 2
    while i< n/2:
        j = 2
        while i*j <= n:
            a[i*j] = 0
            j += 1
        i +=1
    return a
N = int(input('N = '))
A = [i for i in range(N+1)]
res = eratos(A,N)
for i in range(N+1):
    if res[i]:
        print(res[i],end = ' ')