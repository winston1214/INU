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
        print('중간과정1 : ',a)
        quicksort(a,i+1,r) # right
        print('중간과정2 : ',a)

    return a

a = [-1,11,15,7,2,8,5,3,1,6,13,14,9,12,10,4]
l = 1
r = len(a) - 1
quicksort(a,l,r)

def calc_time():
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