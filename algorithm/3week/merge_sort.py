def merge(a,l,m,r):
    b = a.copy()
    i = l
    j = m+1
    k = l
    while i<=m and j <= r:
        if a[i] < a[j]:
            b[k] = a[i]
            k+=1
            i+=1
        else:
            b[k] = a[j]
            k +=1
            j +=1
    if i>m:
        for p in range(j,r+1):
            b[k] = a[p]
            k += 1
    else:
        for p in range(i,m+1):
            a[p] = b[p]
            k+=1
    for p in (l,r+1):
        a[p] = b[p]
    return a

def mergeSort(a,l,r):
    if r>l:
        m = (r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)
    return a
# a = [-1,6,4,2,7,9,3,8,1,10,5]
# l = 1
# r = len(a) - 1
# print(mergeSort(a,l,r))


import time, random
# random.seed(42)
Number = [100000,200000,300000]
for N in Number:
    a = []

    a.append(-1)

    for i in range(N):

        a.append(random.randint(1, N))

    start_time = time.time()
    l = 1
    mergeSort(a, l ,N)

    end_time = time.time() - start_time

    print("합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))