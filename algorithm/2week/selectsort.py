def selectionSort(a,n):
    for i in range(1,n):
        minIndex = i
        for j in range(i+1,n+1):
            if a[minIndex] > a[j]:
                minIndex = j
        a[minIndex],a[i] = a[i],a[minIndex]
        print('중간 결과 : ',a)
    return a
a = [-1,11,15,7,2,8,5,3,1,6,13,14,9,12,10,4]
print(selectionSort(a,len(a)-1))

def calc_time():
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

