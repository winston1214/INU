import time
import random

def shellsort(a,n):
    for h in range(1,n):
        h = 3*h+1
    while h > 0 :
        h = h//3
        if h == 0:
            break
        for i in range(h+1,n+1):
            v = a[i]
            j = i
            while (j>h and a[j-h]>v):
                a[j] = a[j-h]
                j -= h
            a[j] = v
    return a


Number = [5000,10000,15000]
for N in Number:
    a = []

    a.append(None)

    for i in range(N):

        a.append(random.randint(1, N))

    start_time = time.time()

    shellsort(a, N)

    end_time = time.time() - start_time

    print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))