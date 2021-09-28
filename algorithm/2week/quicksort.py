def partition(a,l,r):
    v = a[r]
    i = l
    j = r - 1
    while True:
        while a[i] < v:
            i += 1
        while a[j] >= v:
            j -= 1
        if i >= j: break
        a[i],a[j] = a[j],a[i] # change
    a[i],a[r] = a[r],a[i] # change
    return i

def quicksort(a,l,r):
    if r>l:
        i = partition(a,l,r)

        quicksort(a,l,i-1) # left

        quicksort(a,i+1,r) # right

    return a

# a = [-1,6,4,2,7,9,3,8,1,10,5]
# l = 1
# r = len(a) - 1
# print(quicksort(a,l,r))

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
    quicksort(a, l,N-1)

    end_time = time.time() - start_time

    print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))