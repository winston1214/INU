def bubblesort(a,n):
    for i in range(n,0,-1):
        for j in range(1,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print('중간과정 : ',a)
    return a

a = [-1,11,15,7,2,8,5,3,1,6,13,14,9,12,10,4]
print(bubblesort(a, len(a)-1))

def calc_time():
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