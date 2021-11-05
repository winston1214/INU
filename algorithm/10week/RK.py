def index(c):
    if ord(c) == 32: return 0
    else: return ord(c)-64

def RK(p,t,k):
    dM ,h1,h2 = 1,0,0
    M = len(p)
    N = len(t)
    for i in range(1,M):
        dM = (d * dM) % q
    for i in range(M):
        h1 = (h1 * d + index(p[i])) % q
    i = k
    j = 0
    while i < N and j < M:
        h2 = (h2 * d + index(t[i])) % q
        i += 1
        j += 1
    i = k
    while h1 != h2:
        if i + M > N: return N
        h2 = (h2 + d * q - index(t[i]) * dM) % q
        h2 = (h2 * d + index(t[i+M])) % q
        if i > N - M: return N
        i += 1
    return i
q = 33554393
d = 32
text = 'STRING STARTING CONSISTING'
pattern = 'STING'

M = len(pattern)
N = len(text)
K = 0
while True:
    pos = RK(pattern,text,K)
    K = pos + M
    if K <= N: print('패턴이 나타난 위치 : ', pos)
    else: break
print('END')