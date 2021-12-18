# 합병정렬
def merge(a,l,m,r):
    b = a.copy()
    for i in range(m+1,l,-1):
        b[i-1] = a[i-1]
    i -= 1
    for j in range(m,r):
        b[r+m-j] = a[j+1]
    j += 1
    for k in range(l,r+1):
        if b[i] < b[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = b[j]
            j -= 1
    return a

def mergeSort(a,l,r):
    if r>l:
        m = (r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a,l,m,r)
    return a


def naturalSort(a):
    left = 0
    right = len(a)-1
    l = 0
    r = right
    sorted_bool = False
    while sorted_bool != True:
        sorted_bool = True
        left = 0
        while left < right:
            l = left
            while (l < right and a[l] <= a[l+1]):
                l += 1
            r = l + 1
            while (r == right-1 or r < right and a[r] <= a[r+1]):
                r += 1
            if r <= right:
                merge2(a,left,l,r)
                sorted_bool = False
            left = r+1
    return a
def merge2(a,left,middle,right):
    b = a.copy()
    l = left
    r = middle+1
    for i in range(left,right+1):
        if r > right or (l <= middle and a[l] <= a[r]):
            b[i] = a[l] 
            l += 1  
        elif l> middle or (r <= right and a[r] <= a[l]):
            b[i] = a[r] 
            r += 1       
    
    for i in range(left,right+1):
        a[i] = b[i]
    return a




a = [6, 7, 8, 3, 4, 1, 5, 9, 10, 2]
print(naturalSort(a))

import time
import random
random.seed(42)
Number = [10000,20000,30000]
for N in Number:
    a = []

    a.append(-1)

    for i in range(N):

        a.append(random.randint(1, N))

    start_time = time.time()
    l = 1
    mergeSort(a, l ,N)

    end_time = time.time() - start_time

    print("합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

    
    a = a[1:]
    
    start_time2 = time.time()
    naturalSort(a)
    
    end_time2 = time.time() - start_time2
    print("자연 합병 정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time2))
