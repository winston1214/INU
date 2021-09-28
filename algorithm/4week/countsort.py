def countingSort(a,n,m): # n = len(a), m = a 원소의 최대값
    b = [0]*(n+1)
    count = [0] * (m+1)
    for j in range(1,m+1):
        count[j] = 0

    for i in range(1,n+1):
        count[a[i]] += 1

    for j in range(2,m+1):
        count[j] += count[j-1]

    for i in range(n,0,-1):
        b[count[a[i]]] = a[i]
        count[a[i]] -= 1

    for i in range(1,n+1):
        a[i] = b[i]

    return a

# a = [-1,1,2,2,1,3,4,4,1]
# print(countingSort(a,len(a)-1,max(a)))

import random,time
Number = [100000,200000,300000]
M = 1000
for N in Number:
    a = []

    a.append(None)

    for i in range(N):

        a.append(random.randint(1, M))

    start_time = time.time()
    countingSort(a, N,M)

    end_time = time.time() - start_time

    print("Counting 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))