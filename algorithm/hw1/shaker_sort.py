def shaker_sort(arr,left,right):
    swap = True
    
    while swap == True:
        swap = False
        for i in range(left,right):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        if swap == False: break
        swap = False
        right -= 1
        for i in range(right-1,left-1,-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        left += 1
        
    return arr

def bubblesort(a,n):
    for i in range(n,0,-1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == '__main__':
    import random, time

    Number = [5000,10000,15000]
    for N in Number:
        a = []

        a.append(None)

        for _ in range(N):

            a.append(random.randint(1, N))

        start_time1 = time.time()

        bubblesort(a, N-1)

        end_time1 = time.time() - start_time1

        print("버블 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time1))
        
        a.remove(None)
        start_time2 = time.time()
        shaker_sort(a,0,N-1)
        end_time2 = time.time() - start_time2
        
        print("칵테일 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time2))
