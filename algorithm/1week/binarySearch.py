def binarySearch(a,key,left,right):
    # left, right = left or 0, right or len(a) - 1
    if left <= right:
        mid = (left+right)//2
        if key == mid == left == right:
            print(f'key = {key}, mid = {mid}')
        else:
            print(f'key = {key}, mid = {mid}, right = {right},left = {left}')
        if key == a[mid]: 
            return mid
        if key < a[mid] : return binarySearch(a,key,left,mid-1)
        if key > a[mid] : return binarySearch(a,key,mid+1,right)
    else:

        return -1
Key = int(input('Key = '))
a = [i for i in range(0,50)]
left,right = 1, len(a)-1
print(binarySearch(a,Key,left,right))