import time
import random

def shellsort(a,n):
    for h in range(1,n):
        h = 3*h+1
    while h > 0 :
        h = h//3
        if h == 0:
            break
        for i in range(h+1,n+1):
            v = a[i]
            j = i
            
            while (j>h and a[j-h]>v):
                a[j] = a[j-h]
                j -= h   
            a[j] = v
            print('중간과정 : ',a)            
    return a
# a = [-1,11,15,7,2,8,5,3,1,6,13,14,9,12,10,4]
a = [-1,3,1,14,12,4,10,13,15,5,2,7,9,6,8,11,14]
shellsort(a,len(a)-1)

def calc_time():
    Number = [5000,10000,15000]
    for N in Number:
        a = []

        a.append(None)

        for i in range(N):

            a.append(random.randint(1, N))

        start_time = time.time()

        shellsort(a, N)

        end_time = time.time() - start_time

        print("쉘 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))