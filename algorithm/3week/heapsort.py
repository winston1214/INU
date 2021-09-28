def heapify(a,h,m):
    v = a[h]
    j = 2*h
    while j <=m:
        if (j < m) and (a[j] < a[j+1]):
            j +=1
        if v >= a[j]:
            break
        else:
            a[j//2] = a[j]
        j *= 2
    a[j//2] = v
    return a

def heapSort(a,n):
    for i in range(n//2,0,-1):
        
        heapify(a,i,n)
    for i in range(n-1,0,-1):
        
        a[1],a[i+1] = a[i+1],a[1]
        heapify(a,1,i)
    return a

a = [-1,6,4,2,7,9,3,8,1,10,5]
n = len(a)-1
print(heapSort(a,n))