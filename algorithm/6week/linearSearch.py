class Dict:
    def __init__(self):
        Dict.a = [-1] * M
    def search(self,v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            if v == Dict.a[x]:
                return Dict.a[x]
            else:
                x = (x+1) % M
        return -1
    
    def insert(self,v):
        x = self.hash(v)
        while Dict.a[x] != -1:
            x = (x+1) % M
        Dict.a[x] = v

    def hash(self,v):
        return v % M
    def print(self):
        for i in range(M):
            if Dict.a[i] != -1:
                print('#',end='')
            else:
                print('#',end='')
            if (i+1) % 60 == 0:
                print()
import random,time
N = 10000
M = 10391
key = []
s_key = []
for i in range(N):
    r = random.randint(1,3*N)
    key.append(r)
    s_key.append(r)
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or result != s_key[i]:
        print('탐색오류')
end_time = time.time() - start_time
print('선형 탐사법 실행 시간 (N = %d) : %0.3f'%(N,end_time))
print('탐색완료')