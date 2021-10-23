def partition(a,l,r):
    v = a[r] # pivot
    i = l
    j = r - 1
    print('pivot : ',v)
    while True:
        while a[i] < v:
            i += 1
        while a[j] >= v:
            j -= 1
        if i >= j: break
        a[i],a[j] = a[j],a[i] # change
        print('In While ',a)
    a[i],a[r] = a[r],a[i] # change
    print('Out while ',a)
    print(f'i : {i}')
    return i

def quicksort(a,l,r):
    print('here')
    if r>l:
        print('IN')
        i = partition(a,l,r)
        # print(f'1. l : {l}, r : {r}')
        quicksort(a,l,i-1) # left
        # print('1. ',a)
        # print(f'2. l : {l}, r : {r}')
        # print(i+1,r) # 6 6
        quicksort(a,i+1,r) # right
        # print('2. ',a)
        # print(f'3. l : {l}, r : {r}')

    return a

a = [-1,6,2,8,1,3,9,4,5,10,7]
l = 1
r = len(a) - 1
print(quicksort(a,l,r))

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