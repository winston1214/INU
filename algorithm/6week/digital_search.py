class bitskey:
    def __init__(self, x):
        self.x = x
    def get(self):
        return self.x
    def bits(self, k, j):
        return (self.x >> k) & ~(~0 << j)

class node:
    def __init__(self,key):
        self.key = bitskey(key)
        self.left = None
        self.right = None

class Dict:
    itemMin = bitskey(0)
    z = node(itemMin)
    head = node(itemMin)
    head.left = z
    head.right = z

    def search(self,v):
        v = bitskey(v)
        x = self.head.left
        b = maxb
        self.z.key = v
        while v.get() != x.key.get():
            b -= 1
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
        if x == self.z:
            return -1
        else:
            return x.key.get()
    def insert(self,v):
        v = bitskey(v)
        b = maxb-1
        x = self.head.left
        p = self.head
        while x.key.get() != self.z.key.get():
            p = x
            if v.bits(b,1):
                x = x.right
            else:
                x = x.left
            b -= 1
        x = node(self.itemMin)
        x.key = v
        x.left = self.z
        x.right = self.z
        if v.bits(b+1,1):
            p.right = x
        else:
            p.left = x

# maxb = 14
# arr = [1,19,5,18,3,26,9]
# N = len(arr)
# d = Dict()

# for i in range(N):
#     d.insert(arr[i])
#     d.check(arr[i])



import random,time
N = 10000
maxb = 14
key = list(range(1,N+1))
s_key = list(range(1,N+1))
random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('search error')
end_time = time.time() - start_time
print('디지털 탐색 트리의 실행 시간 (N = %d) : %0.3f'%(N,end_time))
print('Complete')