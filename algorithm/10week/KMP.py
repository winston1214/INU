def initNext(p,m):
    m = len(p)
    next[0] = -1
    i = 0
    j = -1
    while i < M:
        if j != -1 and p[i] == p[j]: next[i] = next[j]
        else: next[i] = j
        while j >= 0 and p[i] != p[j]:
            j = next[j]
        i += 1
        j += 1

def KMP(p,t,k,m,n):
    initNext(p,m)
    i = k
    j = 0
    while j < m and i < n:
        while j >= 0 and t[i] != p[j]:
            j = next[j]
            print(i,j)
        i += 1
        j += 1
    if j == m: return i-m
    else: return i

next = [0] * 50
text = 'ababacabcbababcacacaababca'
pattern = 'ababca'
M = len(pattern)
N = len(text)
K = 0
while True:
    pos = KMP(pattern,text,K,M,N)
    K = pos + M
    if K <= N: print('패턴이 나타난 위치 : ',pos)
    else: 
        text += '/0'
        break
print('스트링 탐색 종료')