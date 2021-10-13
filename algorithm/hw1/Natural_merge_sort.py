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

a = [-1,6,4,2,7,9,3,8,1,10,5]
l = 1
r = len(a) - 1
print(mergeSort(a,l,r))