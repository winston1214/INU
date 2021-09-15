def selectionSort(a,n):
    for i in range(1,n):
        minimum = i
        for j in range(i+1,n):
            if a[j] < a[minimum]:
                minimum = j
        a[j],minimum = minimum,a[j]
    return a


import random, time



Number = [5000,10000,15000]
for N in Number:
    a = []

    a.append(None)

    for i in range(N):

        a.append(random.randint(1, N))

    start_time = time.time()

    selectionSort(a, N)

    end_time = time.time() - start_time

    print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

# checkSort(a, N)