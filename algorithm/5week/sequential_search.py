class node:
    def __init__(self,key=None):
        self.key = key
class Dict:
    def __init__(self):
        Dict.a = []
    def search(self,search_key):
        i = 0
        n = len(Dict.a)
        while i < n and Dict.a[i].key != search_key:
            i += 1
        if i == n :
            return -1
        else:
            return i
    def insert(self,v):
        Dict.a.append(node(v))

import random,time
N = 10000
key  = list(range(1,N+1))
s_key = list(range(1,N+1))
random.shuffle(key)
d = Dict()
for i in range(N):
    d.insert(key[i])
start_time = time.time()
for i in range(N):
    result = d.search(s_key[i])
    if result == -1 or key[result] != s_key[i]:
        print('Search Error')
end_time = time.time() - start_time
print('순차탐색 실행 시간 (N = %d) : %0.3f'%(N,end_time))
print('탐색완료')