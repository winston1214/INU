def bubblesort(a,n):
    for i in range(n,0,-1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# a = [None,3,1,2,4,5]
# print(bubblesort(a,len(a)-1))

import random, time



Number = [5000,10000,15000]
for N in Number:
    a = []

    a.append(None)

    for i in range(N):

        a.append(random.randint(1, N))

    start_time = time.time()

    bubblesort(a, N-1)

    end_time = time.time() - start_time

    print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))