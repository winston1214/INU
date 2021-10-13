def selectionSort(a,n): # 내림차순 변경
    for i in range(1,n):
        minIndex = i
        for j in range(i+1,n+1):
            if a[minIndex] < a[j]:
                minIndex = j
        a[minIndex],a[i] = a[i],a[minIndex]
    return a

def bubblesort(a,n):
    for i in range(n,0,-1):
        for j in range(1,i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

def exchange_sort(arr,N):
    for i in range(N-1):
        for j in range(i+1,N):
            if arr[i] < arr[j]:
                arr[i],arr[j]  = arr[j],arr[i]
    return arr

import random,time

if __name__ == '__main__':
    Number = [5000,10000,15000]
    random.seed(42)
    for N in Number:
        a = []

        a.append(-1)

        for _ in range(N):

            a.append(random.randint(1, N))

        start_time1 = time.time()

        bubblesort(a, N-1)

        end_time1 = time.time() - start_time1

        print("버블 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time1))
        
        start_time2 = time.time()
        selectionSort(a,N-1)
        end_time2 = time.time() - start_time2
        
        a.remove(-1)
        print("선택 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time2))
        start_time3 = time.time()
        exchange_sort(a,N)
        end_time3 = time.time() - start_time3
        print("교환 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time3))