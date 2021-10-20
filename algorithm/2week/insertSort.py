def insertSort(a,n):
    for i in range(2,n+1):
        v = a[i]
        j = i
        while (a[j-1] > v):
            print(f'j = {j}')
            a[j] = a[j-1]
            j = j-1
            
        a[j] = v
        print(f'중간과정 {i} : ',a)
    return a

# a = [-1,11,15,7,2,8,5,3,1,6,13,14,9,12,10,4]
a = [-1,3,2,5,1,4]
print(insertSort(a, len(a)-1))

def cal_time():
    import random, time

    Number = [5000,10000,15000]
    for N in Number:
        a = []

        a.append(-1)

        for i in range(N):

            a.append(random.randint(1, N))

        start_time = time.time()

        insertSort(a, N-1)

        end_time = time.time() - start_time

        print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))